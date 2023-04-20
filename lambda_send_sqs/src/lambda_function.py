import os
import json
import logging.config
import traceback
from contextlib import contextmanager
from typing import Dict
import sqs_message_sender
import log_config

# Define o formato de registro do logger
# LOGGING_CONFIG = log_config.log_config()
# # Configura o logger
# logging.config.dictConfig(LOGGING_CONFIG)


@contextmanager
def handle_exceptions():
    """
    Gerencia exceções em um bloco de código com um contexto 'with'
    """
    try:
        yield
    except KeyError as e:
        logging.error(f"Variável de ambiente ausente: {e}")
        raise Exception("Internal Server Error")
    except Exception as e:
        logging.error(f"Exceção não tratada: {e}\n{traceback.format_exc()}")
        raise Exception("Internal Server Error")


class LambdaHandler:
    def __init__(self, event: Dict, context):
        self.event = event
        self.context = context
        self.queue_url = os.environ.get('SQSqueueUrl')
        self.message_sender = sqs_message_sender.SQSMessageSender(self.queue_url)

    def handle_request(self):
        """
        Processa a solicitação recebida pelo AWS Lambda Function
        """
        logger = logging.getLogger()
        logger.info("request: " + json.dumps(self.event))

        sent_message = self.message_sender.send_message(self.event)

        logger.info(f"Sent message with ID {sent_message['MessageId']}")

        return {
            "statusCode": 200,
            "body": json.dumps(self.event)
        }


def call_handler(event, context):
    """
    Função principal do AWS Lambda Function que processa a solicitação
    """
    with handle_exceptions():
        handler = LambdaHandler(event, context)
        return handler.handle_request()
