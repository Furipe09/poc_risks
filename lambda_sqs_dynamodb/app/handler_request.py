import json
import logging
# import sys
# sys.path.insert(1, '../src')
# from dynamodb import DynamoDB
import dynamodb

logging.basicConfig(level=logging.INFO)


class HandlerRequest:
    try:
        def __init__(self, table_name):
            self.dynamodb = dynamodb.DynamoDB(table_name)

        def handle_request(self, event, context):
            successes = []
            failures = []

            for record in event.get('Records', []):
                logging.info(f"## Registro: {record}")
                payload = json.loads(record.get("body", "{}"))
                if not payload:
                    logging.info("## Requisicao recebida sem payload")
                    message = "Requisicao recebida sem payload"
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
    except Exception as e:
        logging.exception(f"Ocorreu um erro em lambda_request: {e}")
        raise
