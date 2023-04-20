import logging
import json
import boto3
# import log_config
from typing import Dict

# Define o formato de registro do logger
# LOGGING_CONFIG = log_config.log_config()
# # Configura o logger
# logging.config.dictConfig(LOGGING_CONFIG)


class SQSMessageSender:
    def __init__(self, queue_url: str):
        self.sqs_client = boto3.client("sqs")
        self.queue_url = queue_url

    def send_message(self, message_body: Dict):
        try:
            message_body_json = json.dumps(message_body)
            sent_message = self.sqs_client.send_message(
                QueueUrl=self.queue_url,
                MessageBody=message_body_json
            )
            return sent_message

        except Exception as e:
            logging.error(
                f"Erro ao enviar mensagem para a fila {self.queue_url}: {e}")
            raise e
