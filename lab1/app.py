
import json
from flask import Flask, render_template

from database.select import select_dict

app = Flask(__name__)

with open("./data/dbconfig.json") as f:
    app.config['db_config'] = json.load(f)

@app.route("/")
def product_index():
    prod_category = 1
    _sql = f""" SELECT prod_id, prod_name, prod_measure, prod_price, prod_category FROM product
                WHERE prod_category = {prod_category}"""
    result = select_dict(app.config['db_config'], _sql)
    if result:
        prod_title = 'Результаты из БД'
        return render_template("dynamic.html", prod_title=prod_title, products=result)
    else:
        return "No result"

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5001, debug=True)
