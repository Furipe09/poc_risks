import os
import logging
import src.lambda_handler as handler


def lambda_handler(event, context):
    try:

        table_name = os.environ.get('DDB_TABLE')
        lambda_handler = handler.LambdaHandler(table_name)
        return lambda_handler.handle_request(event, context)

    except Exception as e:
        logging.exception(f"Ocorreu um erro em lambda_handler: {e}")
        raise
