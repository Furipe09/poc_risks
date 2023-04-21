variable "dynamodb_table" {
  description = "name of the ddb table"
  type        = string

}

variable "function_name" {
  description = ""
  type        = string
}
variable "SQSqueueArn" {
  description = ""
  type        = string
}
variable "tags" {
  description = ""
  type        = map
}

variable "handler" {
  description = ""
  type        = string
}

variable "runtime" {
  description = ""
  type        = string
}
