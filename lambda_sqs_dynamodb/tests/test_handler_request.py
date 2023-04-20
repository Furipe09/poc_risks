import unittest
from unittest.mock import Mock, patch
import sys
sys.path.insert(1, '../app')
import handler_request


class TestHandlerRequest(unittest.TestCase):
    @patch('handler_request.dynamodb.DynamoDB')
    def test_handle_request_success(self, mock_dynamodb):
        mock_dynamodb_instance = Mock()
        mock_dynamodb_instance.put_item.return_value = None
        mock_dynamodb.return_value = mock_dynamodb_instance
        handler = handler_request.HandlerRequest('approvedRisk')

        event = {'Records': [{'body': '{"IdTransacao": "98",  "IdCliente": "98", "name": "John Does"}'}]}
        result = handler.handle_request(event, {})
        expected_result = {'statusCode': 200, 'headers': {'Content-Type': 'application/json'}, 'body': '{"successes": [{"message": "Dados inseridos com sucesso!"}]}'}
        self.assertEqual(result, expected_result)

    @patch('handler_request.dynamodb.DynamoDB')
    def test_handle_request_failure(self, mock_dynamodb):
        mock_dynamodb_instance = Mock()
        mock_dynamodb_instance.put_item.side_effect = Exception('Test exception')
        mock_dynamodb.return_value = mock_dynamodb_instance
        handler = handler_request.HandlerRequest('approvedRisk')

        event = {'Records': [{'body': '{"IdTransacao": "98",  "IdCliente": "98", "name": "John Does"}'}]}
        result = handler.handle_request(event, {})
        expected_result = {'statusCode': 500, 'headers': {'Content-Type': 'application/json'}, 'body': '{"errors": [{"message": "Erro ao inserir item no DynamoDB"}]}'}
        self.assertEqual(result, expected_result)

    def test_handle_request_empty_payload(self):
        handler = handler_request.HandlerRequest('approvedRisk')

        event = {'Records': [{'body': '{}'}]}
        result = handler.handle_request(event, {})
        expected_result = {'statusCode': 500, 'headers': {'Content-Type': 'application/json'}, 'body': '{"errors": [{"message": "Requisicao recebida sem payload"}]}'}
        self.assertEqual(result, expected_result)

    def test_handle_request_no_records(self):
        handler = handler_request.HandlerRequest('approvedRisk')

        event = {}
        result = handler.handle_request(event, {})
        expected_result = {'statusCode': 200, 'headers': {'Content-Type': 'application/json'}, 'body': '{"successes": []}'}
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
