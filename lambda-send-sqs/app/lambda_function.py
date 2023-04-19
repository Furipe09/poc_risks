import logging
import traceback
from src.lambda_handler import LambdaHandler

# Configura o nível de log para o nível INFO
logging.basicConfig(level=logging.INFO)


def lambda_handler(event, context):
    try:

        # Cria uma instância do LambdaHandler e processa a solicitação
        handler = LambdaHandler(event, context)
        return handler.handle_request()

    # Lida com exceções KeyError, quando uma variável de ambiente está ausente
    except KeyError as e:
        logging.error(f"Variável de ambiente ausente: {e}")
        return {"statusCode": 500, "body": "Internal Server Error"}

    # Lida com qualquer outra exceção não tratada
    except Exception as e:
        logging.error(f"Exceção não tratada: {e}\n{traceback.format_exc()}")
        return {"statusCode": 500, "body": "Internal Server Error"}
