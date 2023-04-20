import os
import logging
from handler_request import HandlerRequest


class LambdaHandler:
    """
    Classe que gerencia a solicitação para um AWS Lambda Function
    """
    def __init__(self, table_name):
        """
        Inicializa a classe LambdaHandler com um objeto HandlerRequest
        """

        try:
            self.lambda_function = HandlerRequest(table_name)
        except Exception as e:
            logging.exception(f"Ocorreu um erro ao inicializar a HandlerRequest: {e}")
            raise

    def handle_request(self, event, context):
        """
        Processa a solicitação recebida pelo AWS Lambda Function usando um objeto HandlerRequest
        """
        try:
            return self.lambda_function.handle_request(event, context)
        except Exception as e:
            logging.exception(f"Ocorreu um erro ao processar a solicitação: {e}")
            raise

    def __enter__(self):
        """
        Método especial chamado quando o objeto é usado em um contexto with
        """
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        """
        Método especial chamado quando o contexto with é finalizado
        """
        # Aqui podemos adicionar código para liberar recursos, se necessário
        pass


def lambda_handler(event, context):
    """
    Função principal do AWS Lambda Function que processa a solicitação
    """
    try:
        table_name = os.environ.get('DDB_TABLE')
        with LambdaHandler(table_name) as handler:
            return handler.handle_request(event, context)

    except Exception as e:
        logging.exception(f"Ocorreu um erro em lambda_handler: {e}")
        raise
