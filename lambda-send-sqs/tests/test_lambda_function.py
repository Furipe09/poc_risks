import json
from unittest.mock import MagicMock
from lambda_handler import LambdaHandler, lambda_handler


def test_lambda_handler():
    # Define o objeto de evento e o contexto para testar o handler
    event = {"message": "Hello World!"}
    context = MagicMock()

    # Cria uma instância do LambdaHandler e processa a solicitação
    handler = LambdaHandler(event, context)
    response = handler.handle_request()

    # Verifica se a resposta é válida
    assert response == {"statusCode": 200, "body": json.dumps(event)}

    # Verifica se a função lambda_handler retorna a mesma resposta que o handler
    assert lambda_handler(event, context) == response
