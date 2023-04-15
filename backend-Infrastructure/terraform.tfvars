# MQ
create_mq              = false
mq_conf_description    = "oneracao Configuration"
mq_conf_name           = "oneracao"
mq_conf_engine_type    = "ActiveMQ"
mq_conf_engine_version = "5.15.0"

# SQS
create_sqs = true
sqs_lambda = "sqs-lambda-Risk"

#Dynamodb
create_dynamodb = true
dynamodb_table  = "approvedRisk"

hash_key          = "IdTransacao"
range_key         = "IdCliente"
IdProduto         = "IdProduto"
IdPropostaProduto = "IdPropostaProduto"
ValorRisco        = "ValorRisco"
ValorParcela      = "ValorParcela"
PrazoContrato     = "PrazoContrato"
ValidadeProposta  = "ValidadeProposta"
