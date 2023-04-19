import json
from unittest.mock import MagicMock
from src.lambda_handler import LambdaHandler


def test_handle_request_success():
    # Mock do evento recebido pelo Lambda
    event = {
        "key1": "value1",
        "key2": "value2"
    }

    # Mock do contexto do Lambda
    context = MagicMock()

    # Mock do objeto SQSMessageSender
    message_sender_mock = MagicMock()
    message_sender_mock.send_message.return_value = {"MessageId": "mocked_id"}

    # Cria instância do LambdaHandler com mocks
    lambda_handler = LambdaHandler(event, context)
    lambda_handler.message_sender = message_sender_mock

    # Chama a função handle_request()
    response = lambda_handler.handle_request()

    # Verifica se o retorno da função está correto
    assert response == {
        "statusCode": 200,
        "body": json.dumps(event)
    }

    # Verifica se a função send_message() do SQSMessageSender foi chamada corretamente
    message_sender_mock.send_message.assert_called_once_with(event)


def test_handle_request_error():
    # Mock do evento recebido pelo Lambda
    event = {
        "key1": "value1",
        "key2": "value2"
    }

    # Mock do contexto do Lambda
    context = MagicMock()

    # Mock do objeto SQSMessageSender que gera exceção
    message_sender_mock = MagicMock()
    message_sender_mock.send_message.side_effect = Exception("Error sending message to SQS")

    # Cria instância do LambdaHandler com mocks
    lambda_handler = LambdaHandler(event, context)
    lambda_handler.message_sender = message_sender_mock

    # Chama a função handle_request()
    response = lambda_handler.handle_request()

    # Verifica se o retorno da função está correto
    assert response == {
        "statusCode": 500,
        "body": json.dumps({"error": "Internal Server Error"})
    }

    # Verifica se a função send_message() do SQSMessageSender foi chamada corretamente
    message_sender_mock.send_message.assert_called_once_with(event)
