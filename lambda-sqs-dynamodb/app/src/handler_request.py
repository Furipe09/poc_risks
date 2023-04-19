import json
import logging
from src.dynamodb import DynamoDB

logging.basicConfig(level=logging.INFO)


class HandlerRequest:
    def __init__(self, table_name):
        self.dynamodb = DynamoDB(table_name)

    def handle_request(self, event, context):
        successes = []
        failures = []

        for record in event.get('Records', []):
            logging.info(f"## Registro: {record}")
            payload = json.loads(record.get("body", "{}"))
            if not payload:
                logging.info("## Requisição recebida sem payload")
                message = "Requisição recebida sem payload"
                failures.append({"message": message})
                continue

            logging.info(f"## Payload Recebido: {payload}")
            try:
                self.dynamodb.put_item(payload)
            except Exception as e:
                logging.error(f"Erro ao inserir item no DynamoDB: {e}")
                message = "Erro ao inserir item no DynamoDB"
                failures.append({"message": message})
            else:
                message = "Dados inseridos com sucesso!"
                successes.append({"message": message})

        if failures:
            return {
                "statusCode": 500,
                "headers": {
                    "Content-Type": "application/json"
                },
                "body": json.dumps({"errors": failures})
            }
        else:
            return {
                "statusCode": 200,
                "headers": {
                    "Content-Type": "application/json"
                },
                "body": json.dumps({"successes": successes})
            }
