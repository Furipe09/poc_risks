import json
import pytest
from unittest.mock import MagicMock, patch

from src.lambda_handler import LambdaHandler


@pytest.fixture
def table_name():
    return "my_table_name"


@pytest.fixture
def handler(table_name):
    return LambdaHandler(table_name)


def test_lambda_handler_initialization(table_name, handler):
    assert handler.table_name == table_name


@patch('src.lambda_handler.Request.HandlerRequest', autospec=True)
def test_lambda_handler_handle_request(mock_request_handler, handler):
    mock_request_handler_instance = MagicMock()
    mock_request_handler_instance.handle_request.return_value = {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps({"successes": []})
    }
    mock_request_handler.return_value = mock_request_handler_instance

    event = {"Records": [{"body": '{"field1": "value1", "field2": "value2"}'}]}
    context = MagicMock()

    response = handler.handle_request(event, context)

    mock_request_handler.assert_called_once_with(table_name=handler.table_name)
    mock_request_handler_instance.handle_request.assert_called_once_with(event, context)

    assert response == {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps({"successes": []})
    }
