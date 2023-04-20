import unittest
from unittest.mock import MagicMock, patch
import sys
sys.path.insert(1, '../app')
import lambda_function


class TestLambdaHandler(unittest.TestCase):
    def setUp(self):
        self.event = {}
        self.context = MagicMock()
        self.table_name = "my-table-name"

    @patch("lambda_function.HandlerRequest")
    def test_initialization(self, MockHandlerRequest):
        # Teste de inicialização da classe LambdaHandler
        handler = lambda_function.LambdaHandler(self.table_name)
        MockHandlerRequest.assert_called_once_with(self.table_name)
        self.assertIsNotNone(handler.lambda_function)

    @patch("lambda_function.HandlerRequest")
    def test_handle_request(self, MockHandlerRequest):
        # Teste do método handle_request da classe LambdaHandler
        handler = lambda_function.LambdaHandler(self.table_name)
        handler.lambda_function.handle_request.return_value = "success"
        result = handler.handle_request(self.event, self.context)
        self.assertEqual(result, "success")

    @patch("lambda_function.logging.exception")
    @patch("lambda_function.HandlerRequest")
    def test_handle_request_with_exception(self, MockHandlerRequest, mock_logging):
        # Teste do método handle_request da classe LambdaHandler com tratamento de exceção
        handler = lambda_function.LambdaHandler(self.table_name)
        handler.lambda_function.handle_request.side_effect = Exception("error")
        with self.assertRaises(Exception):
            handler.handle_request(self.event, self.context)
        mock_logging.assert_called_once()
