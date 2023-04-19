import logging
import json
import os
from src.sqs_message_sender import SQSMessageSender


class LambdaHandler:
    def __init__(self, event, context):
        # Inicializa a instância do LambdaHandler com o evento e o contexto
        self.event = event
        self.context = context

        # Recupera a URL da fila SQS das variáveis de ambiente
        self.queue_url = os.environ.get('SQSqueueUrl')

        # Inicializa a instância do SQSMessageSender com a URL da fila
        self.message_sender = SQSMessageSender(self.queue_url)

    def handle_request(self):
        # Obtém a instância do logger
        logger = logging.getLogger()

        # Registra o evento da solicitação
        logger.info("request: " + json.dumps(self.event))

        try:
            # Envia a mensagem para a fila SQS
            sent_message = self.message_sender.send_message(self.event)

            # Registra o sucesso do envio da mensagem
            logger.info(f"Sent message with ID {sent_message['MessageId']}")

            return {
                "statusCode": 200,
                "body": json.dumps(self.event)
            }
        except Exception as e:
            # Registra o erro de envio da mensagem
            logger.error(f"Error sending message to SQS: {str(e)}")

            # Retorna a mensagem de erro para o chamador
            return {
                "statusCode": 500,
                "body": json.dumps({"error": "Internal Server Error"})
            }
