# POC de Gestão de Riscos

Essa POC tem como objetivo enviar mensagens SQS de uma lambda, recepcionar mensagem do SQS em outra Lambda e gravar na tabela DB2

Os recursos de Infra abaixo foram criados no diretório 'Terraform-Infra':
- DynamoDB Table
- SQS Queue

A Lambda que envia mensagem ao SQS foi criada no diretório 'Terraform-Lambda-Send-SQS'

A Lambda que escuta e recebe as mensagem do SQS e grava no DynamoDB está no diretório 'Terraform-SQS-Lambda-DynamoDB'

Para executar essa POC:
    Em Desenvolvimento...