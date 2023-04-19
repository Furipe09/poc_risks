import boto3
import logging

logging.basicConfig(level=logging.INFO)


class DynamoDB:
    def __init__(self, table_name):
        self.dynamodb = boto3.resource('dynamodb')
        self.table = self.dynamodb.Table(table_name)
        logging.info(f"## Tabela da variável environment DDB_TABLE: {table_name}")

    def put_item(self, item):
        try:
            response = self.table.put_item(Item=item)
            logging.info(f"## Item inserido na tabela {self.table.name}: {response}")
        except Exception as e:
            logging.error(f"Erro ao inserir item na tabela {self.table.name}: {e}")
            raise e
