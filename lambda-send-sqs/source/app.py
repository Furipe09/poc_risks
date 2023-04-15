import logging
import json
import boto3
import os

from botocore.exceptions import ClientError


class SQSMessageSender:
    def __init__(self, queue_url):
        self.sqs_client = boto3.client("sqs")
        self.queue_url = queue_url

    def send_message(self, message_body):
        try:
            sent_message = self.sqs_client.send_message(
                QueueUrl=self.queue_url,
                MessageBody=json.dumps(message_body)
            )

            return sent_message

        except ClientError as e:
            logging.error(
                f"Error sending message to queue {self.queue_url}: {e}")
            raise e


def lambda_handler(event, context):
    queue_url = os.environ.get('SQSqueueUrl')
    message_sender = SQSMessageSender(queue_url)

    logger = logging.getLogger()
    logger.info("request: " + json.dumps(event))

    sent_message = message_sender.send_message(event)

    logger.info(f"Sent message with ID {sent_message['MessageId']}")

    return {
        "statusCode": 200,
        "body": json.dumps(event)
    }
