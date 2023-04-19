import json
from unittest.mock import MagicMock
from src.handler_request import HandlerRequest


def test_handler_request_successful():
    # Dados de entrada
    event = {
        "Records": [
            {"body": json.dumps({"id": 1, "name": "John Doe"})},
            {"body": json.dumps({"id": 2, "name": "Jane Doe"})}
        ]
    }
    context = MagicMock()

    # Objeto HandlerRequest
    handler_request = HandlerRequest(table_name="test_table")

    # Chamada do método handle_request
    response = handler_request.handle_request(event, context)

    # Verifica se a resposta é válida
    assert response["statusCode"] == 200
    assert response["headers"]["Content-Type"] == "application/json"
    assert "successes" in response

def test_handler_request_no_payload():
    # Dados de entrada
    event = {
        "Records": [
            {"body": ""}
        ]
    }
    context = MagicMock()

    # Objeto HandlerRequest
    handler_request = HandlerRequest(table_name="test_table")

    # Chamada do método handle_request
    response = handler_request.handle_request(event, context)

    # Verifica se a resposta é válida
    assert response["statusCode"] == 500
    assert response["headers"]["Content-Type"] == "application/json"
    assert "errors" in response

def test_handler_request_exception():
    # Dados de entrada
    event = {
        "Records": [
            {"body": json.dumps({"id": 1, "name": "John Doe"})},
            {"body": json.dumps({"id": 2, "name": "Jane Doe"})}
        ]
    }
    context = MagicMock()

    # Objeto HandlerRequest com método put_item mockado para gerar exceção
    handler_request = HandlerRequest(table_name="test_table")
    handler_request.dynamodb.put_item = MagicMock(side_effect=Exception("Erro"))

    # Chamada do método handle_request
    response = handler_request.handle_request(event, context)

    # Verifica se a resposta é válida
    assert response["statusCode"] == 500
    assert response["headers"]["Content-Type"] == "application/json"
    assert "errors" in response
