import boto3
import os
import json
import logging

logging.basicConfig(level=logging.INFO)


class DynamoDB:
    def __init__(self, table_name):
        self.dynamodb = boto3.resource('dynamodb')
        self.table = self.dynamodb.Table(table_name)
        logging.info(
            f"## Tabela da variável environment DDB_TABLE: {table_name}")

    def put_item(self, item):
        self.table.put_item(Item=item)


class LambdaFunction:
    def __init__(self, table_name):
        self.dynamodb = DynamoDB(table_name)

    def handle_request(self, event, context):
        for record in event['Records']:
            logging.info(f"## Registro: {record}")

            if record["body"]:
                payload = json.loads(record["body"])
                logging.info(f"## Payload Recebido: {payload}")
                self.dynamodb.put_item(payload)

                message = "Dados inseridos com sucesso!"
                return {
                    "statusCode": 200,
                    "headers": {
                        "Content-Type": "application/json"
                    },
                    "body": json.dumps({"message": message})
                }
            else:
                logging.info("## Requisição recebida sem payload")
                message = "Requisição recebida sem payload"
                return {
                    "statusCode": 204,
                    "headers": {
                        "Content-Type": "application/json"
                    },
                    "body": json.dumps({"message": message})
                }


def lambda_handler(event, context):
    tableName = os.environ.get('DDB_TABLE')
    lambda_function = LambdaFunction(tableName)
    return lambda_function.handle_request(event, context)
