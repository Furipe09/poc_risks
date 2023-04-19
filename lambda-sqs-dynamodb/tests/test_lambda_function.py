import os
from unittest import mock
from app.src.lambda_handler import lambda_handler


@mock.patch('src.lambda_function.handler.LambdaHandler.handle_request')
def test_lambda_handler(mock_handle_request):
    event = {'Records': [{'body': '{"name": "John Doe", "age": 30}'}]}
    context = {}
    os.environ['DDB_TABLE'] = 'test-table'

    # test successful response
    mock_handle_request.return_value = {
        'statusCode': 200,
        'headers': {'Content-Type': 'application/json'},
        'body': '{"successes": [{"message": "Dados inseridos com sucesso!"}]}'
    }
    response = lambda_handler(event, context)
    assert response['statusCode'] == 200
    assert response['body'] == '{"successes": [{"message": "Dados inseridos com sucesso!"}]}'

    # test failure response
    mock_handle_request.return_value = {
        'statusCode': 500,
        'headers': {'Content-Type': 'application/json'},
        'body': '{"errors": [{"message": "Erro ao inserir item no DynamoDB"}]}'
    }
    response = lambda_handler(event, context)
    assert response['statusCode'] == 500
    assert response['body'] == '{"errors": [{"message": "Erro ao inserir item no DynamoDB"}]}'


@mock.patch('src.lambda_function.handler.LambdaHandler.handle_request', side_effect=Exception('Test Exception'))
def test_lambda_handler_exception(mock_handle_request):
    event = {'Records': [{'body': '{"name": "John Doe", "age": 30}'}]}
    context = {}
    os.environ['DDB_TABLE'] = 'test-table'

    # test exception
    try:
        response = lambda_handler(event, context)
    except Exception as e:
        assert str(e) == 'Test Exception'
