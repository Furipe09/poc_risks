import logging
import json
import boto3


class SQSMessageSender:
    def __init__(self, queue_url):
        """
        Construtor que inicializa a instância da classe SQSMessageSender.

        Args:
            queue_url (str): URL da fila SQS.

        """
        # Inicializa o cliente SQS da biblioteca boto3
        self.sqs_client = boto3.client("sqs")
        # Armazena a URL da fila SQS
        self.queue_url = queue_url

    def send_message(self, message_body):
        """
        Método que envia uma mensagem para a fila SQS.

        Args:
            message_body (dict):
            corpo da mensagem que será enviado para a fila SQS.

        Returns:
            dict:
            um dicionário que contém informações sobre a mensagem enviada.

        Raises:
            Exception: se houver um erro ao enviar a mensagem para a fila SQS.

        """
        try:
            # Converte o corpo da mensagem em um formato JSON
            message_body_json = json.dumps(message_body)
            # Envia a mensagem para a fila SQS usando o cliente SQS
            # da biblioteca boto3
            sent_message = self.sqs_client.send_message(
                QueueUrl=self.queue_url,
                MessageBody=message_body_json
            )

            # Retorna o objeto de mensagem enviada
            return sent_message

        except Exception as e:
            # Registra um erro usando o módulo de registro de logs do Python
            logging.error(
                f"Erro ao enviar mensagem para a fila {self.queue_url}: {e}")
            # Relança a exceção para propagá-la ao chamador do método
            raise e
