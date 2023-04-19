import src.handler_request as Request


class LambdaHandler:
    def __init__(self, table_name):
        self.table_name = table_name
        try:
            self.lambda_function = Request.HandlerRequest(self.table_name)
        except Exception as e:
            print(f"Ocorreu um erro ao inicializar a HandlerRequest: {e}")
            raise

    def handle_request(self, event, context):
        try:
            # Processar a solicitação usando o HandlerRequest
            return self.lambda_function.handle_request(event, context)
        except Exception as e:
            print(f"Ocorreu um erro ao processar a solicitacao: {e}")
            raise
