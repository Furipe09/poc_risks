variable "dynamodb_table" {
  description = "name of the ddb table"
  type        = string
  default     = "approvedRisk"

}

variable "SQSqueueArn" {
  description = ""
  type        = string
  default     = "arn:aws:sqs:us-east-1:222497770433:sqs-lambda-Risk"
}