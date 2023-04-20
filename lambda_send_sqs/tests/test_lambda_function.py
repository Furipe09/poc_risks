import unittest
from unittest.mock import MagicMock, patch
import sys
sys.path.insert(1, '../src')

import lambda_function


class TestLambdaHandler(unittest.TestCase):

    def test_handle_request(self):
        mock_event = {"key": "value"}
        mock_context = MagicMock()
        mock_send_message = MagicMock(return_value={"MessageId": "123"})
        with patch("lambda_function.sqs_message_sender.SQSMessageSender.send_message", mock_send_message):
            handler = lambda_function.LambdaHandler(mock_event, mock_context)
            response = handler.handle_request()
            self.assertEqual(response["statusCode"], 200)
            self.assertEqual(response["body"], '{"key": "value"}')
            mock_send_message.assert_called_once_with(mock_event)

    def test_call_handler(self):
        mock_event = {"key": "value"}
        mock_context = MagicMock()
        with patch("lambda_function.LambdaHandler.handle_request") as mock_handle_request:
            mock_handle_request.return_value = {"statusCode": 200, "body": "OK"}
            response = lambda_function.call_handler(mock_event, mock_context)
            self.assertEqual(response["statusCode"], 200)
            self.assertEqual(response["body"], "OK")
            mock_handle_request.assert_called_once_with()

if __name__ == '__main__':
    unittest.main()
