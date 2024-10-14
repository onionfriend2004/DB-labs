
import json
import os

from flask import Flask, render_template, request

from database.select import select_list
from database.sql_provider import SQLProvider

app = Flask(__name__)

with open("./data/dbconfig.json") as f:
    app.config['db_config'] = json.load(f)

provider = SQLProvider(os.path.join(os.path.dirname(__file__), 'sql'))

@app.route("/", methods=['GET', 'POST'])
def product_index():
    if request.method == "GET":
        return render_template("input_category.html")
    else:
        prod_category = request.form.get('prod_category')

        # Проверка наличия параметра
        if not prod_category:
            return "Error: Category parameter is missing"

        # Проверка, что параметр является целым числом
        if not prod_category.isdigit():
            return "Error: Category must be an integer"

        try:
            _sql = provider.get('product.sql', prod_category=prod_category)
            result, schema = select_list(app.config['db_config'], _sql)
            print("res_info.result = ", result)
            # Проверка наличия данных в результате
            if not result:
                return "No result"

            prod_title = 'Результаты из БД'
            return render_template("dynamic.html", prod_title=prod_title, products=result)
        except Exception as e:
            # Логирование ошибок
            app.logger.error(f"Error executing SQL query: {e}")
            return "Error: An error occurred while processing your request"
        
if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5001, debug=True)
