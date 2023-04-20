# Risks POC

## Essa POC tem como objetivo:
- Enviar mensagens SQS de uma lambda, 
- Recepcionar mensagem do SQS em outra Lambda e gravar na tabela DynamoDB

### Os recursos de Infra abaixo foram criados no diretório 'backend-Infrastructure':
- DynamoDB Table
- SQS Queue

- Lambda - Envia mensagem ao SQS foi criada no diretório 'lambda-send-sqs'

 - Lambda - Escuta e recebe as mensagem do SQS e grava no DynamoDB está no diretório 'lambda-sqs-dynamodb'

## Para executar essa POC:
1. Executar o passo a passo do backen-Infrastructure/README.md
2. Executar o passo a passo do lambda-send-sqs/README.md
3. Executar o passo a passo do lambda-sqs-dynamodb/README.md