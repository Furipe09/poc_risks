import json
import boto3
from unittest import mock
from src.sqs_message_sender import SQSMessageSender

class TestSQSMessageSender:
    def test_send_message(self, monkeypatch):
        # Cria um mock do cliente SQS da biblioteca boto3
        mock_sqs_client = mock.Mock()
        # Define o retorno do método send_message do mock do cliente SQS
        mock_sqs_client.send_message.return_value = {
            "MessageId": "mock_message_id",
            "MD5OfMessageBody": "mock_md5"
        }
        # Aplica o mock do cliente SQS no contexto do teste utilizando o monkeypatch do pytest
        monkeypatch.setattr(boto3, "client", lambda service_name: mock_sqs_client)

        # Define uma URL de fila de teste
        queue_url = "mock_queue_url"
        # Cria uma instância do SQSMessageSender com a URL de fila de teste
        sender = SQSMessageSender(queue_url)
        # Define um corpo de mensagem de teste
        message_body = {"foo": "bar"}

        # Chama o método send_message da instância do SQSMessageSender
        sent_message = sender.send_message(message_body)

        # Verifica se o retorno do método é um dicionário contendo o ID da mensagem e o MD5 do corpo da mensagem
        assert isinstance(sent_message, dict)
        assert "MessageId" in sent_message
        assert "MD5OfMessageBody" in sent_message

        # Verifica se o método send_message do cliente SQS foi chamado corretamente
        mock_sqs_client.send_message.assert_called_once_with(
            QueueUrl=queue_url,
            MessageBody=json.dumps(message_body)
        )
