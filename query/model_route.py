from dataclasses import dataclass
from database.select import select_list

@dataclass
class ProductInfoResponse:
    result: tuple
    error_message: str
    status: bool

def fetch_categories(db_config, sql_provider):
    error_message = ''
    _sql = sql_provider.get('category.sql')
    result, schema = select_list(db_config, _sql)

    if result:
        return ProductInfoResponse([category[0] for category in result], error_message=error_message, status=True)
    result = ()
    error_message = "Error: can't connect to db"
    return ProductInfoResponse(result, error_message=error_message, status=False)

def category_info(db_config, user_input_data, sql_provider):
    error_message = ''
    prod_category = user_input_data.get('prod_category')
    print(prod_category)
    # Проверка наличия категории
    if not prod_category:
        error_message = "Error: Category parameter is missing"
        result = ()
        return ProductInfoResponse(result, error_message=error_message, status=False)

    # Получаем SQL с учетом строкового значения категории
    _sql = sql_provider.get('product.sql', prod_category=prod_category)

    result, schema = select_list(db_config, _sql)
    print(result)
    if not result:
        error_message = "No result"
        return ProductInfoResponse(result, error_message=error_message, status=False)

    return ProductInfoResponse(result, error_message=error_message, status=True)

