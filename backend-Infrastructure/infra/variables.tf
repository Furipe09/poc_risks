############################ MQ ##

# variable "create_mq" {
#   description = ""
#   type        = bool
#   default     = false
# }

# variable "mq_conf_description" {
#   description = ""
#   type        = string
#   default     = "oneracao Configuration"
# }

# variable "mq_conf_name" {
#   description = ""
#   type        = string
#   default     = "oneracao"
# }

# variable "mq_conf_engine_type" {
#   description = ""
#   type        = string
#   default     = "ActiveMQ"
# }

# variable "mq_conf_engine_version" {
#   description = ""
#   type        = string
#   default     = "5.15.0"
# }

# variable "mq_broker_name" {
#   description = ""
#   type        = string
#   default     = "oneracao"
# }

# variable "mq_host_instance_type" {
#   description = ""
#   type        = string
#   default     = "mq.t2.micro"
# }

# variable "mq_username" {
#   description = ""
#   type        = string
#   default     = ""
# }

# variable "mq_password" {
#   description = ""
#   type        = string
#   default     = ""
# }

########################### SQS ##

variable "create_sqs" {
  description = ""
  type        = bool
  default     = false
}

variable "sqs_lambda" {
  description = "name SQS queue"
  type        = string
  default     = "sqs-lambda-Risk"
}

############################ Dynamodb ##

variable "create_dynamodb" {
  description = ""
  type        = bool
  default     = false
}

variable "dynamodb_table" {
  description = "name of the ddb table"
  type        = string
  default     = "approvedRisk"
}

variable "hash_key" {
  description = "Codigo da proposta do produto"
  type        = string
  default     = "IdTransacao"
}

variable "range_key" {
  description = "Id Cliente"
  type        = string
  default     = "IdCliente"
}

# variable "IdProduto" {
#   description = "Codigo do produto"
#   type        = string
#   default     = "IdProduto"
# }

# variable "IdPropostaProduto" {
#   description = "Codigo da proposta do produto"
#   type        = string
#   default     = "IdPropostaProduto"
# }

# variable "ValorRisco" {
#   description = "Codigo da proposta do produto"
#   type        = string
#   default     = "ValorRisco"
# }

# variable "ValorParcela" {
#   description = "Codigo da proposta do produto"
#   type        = string
#   default     = "ValorParcela"
# }

# variable "PrazoContrato" {
#   description = "Codigo da proposta do produto"
#   type        = string
#   default     = "PrazoContrato"
# }

# variable "ValidadeProposta" {
#   description = "Codigo da proposta do produto"
#   type        = string
#   default     = "ValidadeProposta"
# }


# variable "broker_engine_type" {
#   description = ""
#   type        = string
#   default     = ""
# }

# variable "broker_engine_version" {
#   description = ""
#   type        = string
#   default     = ""
# }
