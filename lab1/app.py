import json
import os

from flask import Flask, render_template, request

from database.sql_provider import SQLProvider
from model_route import model_route, fetch_categories

app = Flask(__name__)

with open("./data/dbconfig.json") as f:
    app.config['db_config'] = json.load(f)

provider = SQLProvider(os.path.join(os.path.dirname(__file__), 'sql'))

@app.route('/', methods=['GET'])
def product_handler():
    response = fetch_categories(app.config['db_config'], provider)
    if response.status:
        return render_template("input_category.html", categories=response.result)
    else:
        return response.error_message, 500

@app.route("/", methods=['POST'])
def product_result_handler():
    user_input_data = request.form.to_dict()
    print(f"User input data: {user_input_data}") 
    response = model_route(app.config['db_config'], user_input_data, provider)

    if not response.status:
        return response.error_message, 500

    prod_title = 'Результаты из БД'
    return render_template("dynamic.html", prod_title=prod_title, products=response.result)

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5001, debug=True)
