from dataclasses import dataclass
from database.select import select_list

@dataclass
class ProductInfoResponse:
    result: tuple
    error_message: str
    status: bool

def model_route(db_config, user_input_data, sql_provider):
    error_message = ''
    prod_category = user_input_data.get('prod_category')

    # Проверка наличия параметра
    if not prod_category:
        error_message = "Error: Category parameter is missing"
        result = ()
        return ProductInfoResponse(result, error_message=error_message, status=False)

    # Проверка, что параметр является целым числом
    if not prod_category.isdigit():
        error_message = "Error: Category must be an integer"
        result = ()
        return ProductInfoResponse(result, error_message=error_message, status=False)

    try:
        _sql = sql_provider.get('product.sql', prod_category=prod_category)
        result, schema = select_list(db_config, _sql)
        print("res_info.result = ", result)
        # Проверка наличия данных в результате
        if not result:
            error_message = "No result"
            return ProductInfoResponse(result, error_message=error_message, status=False)

        return ProductInfoResponse(result, error_message=error_message, status=True)
    except Exception as e:
        # Логирование ошибок
        error_message = f"Error executing SQL query: {e}"
        result = ()
        return ProductInfoResponse(result, error_message=error_message, status=False)