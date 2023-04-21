variable "dynamodb_table" {
  description = "name of the ddb table"
  type        = string
  default = "approvedRisk"
}

variable "function_name" {
  description = ""
  type        = string
  default = "SQSLambdaToDynamodb"
}
variable "SQSqueueArn" {
  description = ""
  type        = string
  default = "sqs-lambda-Risk"
}
variable "tags" {
  description = ""
  type        = map
  default = { "project" = "risk" }
}

variable "handler" {
  description = ""
  type        = string
  default = "lambda_function.lambda_handler"
}

variable "runtime" {
  description = ""
  type        = string
  default = "python3.9"
}
