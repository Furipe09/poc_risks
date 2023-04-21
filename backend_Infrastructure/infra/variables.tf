########################### SQS ##

variable "create_sqs" {
  description = ""
  type        = bool
  default     = true
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
  default     = true
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
variable "dynamodb_billing_mode" {
  description = ""
  type        = string
  default = "PROVISIONED"
}

variable "dynamodb_read_capacity" {
  description = ""
  type        = string
  default = 20
}

variable "dynamodb_write_capacity" {
  description = ""
  default = 20
}

variable "tags" {
  description = ""
  type        = map
  default     = { "project" = "risk" }
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
