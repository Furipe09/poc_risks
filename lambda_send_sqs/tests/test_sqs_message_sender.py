import unittest
from unittest.mock import MagicMock
import sys
sys.path.insert(1, '../src')

from sqs_message_sender import SQSMessageSender


class TestSQSMessageSender(unittest.TestCase):

    def setUp(self):
        self.mock_sqs_client = MagicMock()
        self.queue_url = 'my_queue_url'
        self.message_body = {'message': 'test message'}
        self.sender = SQSMessageSender(self.queue_url)
        self.sender.sqs_client = self.mock_sqs_client

    def test_send_message_success(self):
        self.mock_sqs_client.send_message.return_value = {'MessageId': 'test_id'}
        response = self.sender.send_message(self.message_body)
        self.assertEqual(response, {'MessageId': 'test_id'})
        self.mock_sqs_client.send_message.assert_called_with(QueueUrl=self.queue_url,
                                                             MessageBody='{"message": "test message"}')

    def test_send_message_failure(self):
        self.mock_sqs_client.send_message.side_effect = Exception('test error')
        with self.assertRaises(Exception):
            self.sender.send_message(self.message_body)
        self.mock_sqs_client.send_message.assert_called_with(QueueUrl=self.queue_url,
                                                             MessageBody='{"message": "test message"}')
