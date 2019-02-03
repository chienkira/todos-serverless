import json
from functools import wraps
from handlers.lib.decimalencoder import DecimalEncoder


def handle_api_response(func):
    @wraps(func)
    def wrapped_func(*args, **kwargs):
        try:
            response = func(*args, **kwargs)
            return {
                'statusCode': 200,
                'body': json.dumps(response, cls=DecimalEncoder)
            }
        except Exception as e:
            return {
                'statusCode': 500,
                'body': str(e)
            }

    return wrapped_func
