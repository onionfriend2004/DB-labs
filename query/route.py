
import os
from flask import Flask, render_template, Blueprint, current_app, request
from query.model_route import category_info, fetch_categories

from access import group_required


blueprint_query = Blueprint('query_bp', __name__, template_folder='templates')

from database.sql_provider import SQLProvider

blueprint_query = Blueprint('query_bp', __name__, template_folder='templates')

provider = SQLProvider(os.path.join(os.path.dirname(__file__), 'sql'))

@blueprint_query.route('/', methods=['GET'])
@group_required
def product_handler():
    response = fetch_categories(current_app.config['db_config'], provider)
    if response.status:
        return render_template("input_category.html", categories=response.result)
    else:
        return response.error_message

@blueprint_query.route('/', methods=['POST'])
@group_required
def product_result_handler():
    user_input_data = request.form.to_dict()
    print(f"User input data: {user_input_data}") 
    response = category_info(current_app.config['db_config'], user_input_data, provider)
    print(response.result)
    if not response.status:
        return response.error_message

    prod_title = 'Результаты из БД'
    return render_template("dynamic.html", prod_title=prod_title, products=response.result)