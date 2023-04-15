
import boto3
import os
import json
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event, context):
    
  tableName = os.environ.get('DDB_TABLE')
  dynamodb = boto3.resource('dynamodb')
  table =  dynamodb.Table(tableName)
  logging.info(f"## Tabela da variável environment DDB_TABLE: {table}")
  
  try:
      for record in event['Records']:
        logging.info(f"## Registro: {record}")
        
        if record["body"]:
            payload = json.loads(record["body"])
            logging.info(f"## Payload Recebido: {payload}")
            table.put_item(Item=payload)

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
            # dynamodb.put_item(TableName=table,Item={"userId": {'S':'2012'}, "name": {'S':'The Amazing Spider-Man 2'}})
            # message = "Dados inseridos com sucesso!"
            return {
                "statusCode": 204,
                "headers": {
                    "Content-Type": "application/json"
                },
                "body": json.dumps({"message": message})
            }
  except Exception as e:
      print( f"Erro - {e}")
      print( f"Erro no Insert do payload - {payload}")

