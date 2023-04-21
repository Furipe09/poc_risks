variable "SQSqueueUrl" {
  description = ""
  type        = string
  default     = "sqs-lambda-Risk"
}

variable "function_name" {
  description = ""
  type        = string
  default     = "LambdaToSQS"
}

variable "runtime" {
  description = ""
  type        = string
  default     = "python3.9"
}

variable "handler" {
  description = ""
  type        = string
  default     = "lambda_function.call_handler"
}
variable "tags" {
  description = ""
  type        = map
  default     = { "project" = "risk" }
}