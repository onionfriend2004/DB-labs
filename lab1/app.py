
import json
import os

from flask import Flask, render_template, request

from database.select import select_dict
from database.sql_provider import SQLProvider
from model_route import model_route

app = Flask(__name__)
with open("./data/dbconfig.json") as f:
    app.config['db_config'] = json.load(f)

provider = SQLProvider(os.path.join(os.path.dirname(__file__), 'sql'))

@app.route('/', methods=['GET'])
def product_handler():
    return render_template("input_category.html")

@app.route("/", methods=['POST'])
def product_result_handler():
    user_data = request.form
    print(user_data)
    res_info = model_route(app.config['db_config'], user_data, provider)
    print("res_info.result = ", res_info.result)
    if res_info.status:
        prod_title = 'Результаты из БД'
        return render_template("dynamic.html", prod_title=prod_title, products=res_info.result)
    else:
        return "No result"

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5001, debug=True)
