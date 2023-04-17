variable "queue_url" {
  description = ""
  type        = string
  default     = "arn:aws:mq:us-east-1:222497770433:broker:example:b-7032bcbe-8bb0-4a4c-b78f-dae581bbe31c"
}

variable "brokerid" {
  type        = string
  description = ""
  default     = ""
}

variable "username" {
  type        = string
  description = ""
  default     = ""
}

variable "password" {
  type        = string
  description = ""
  default     = ""
}

variable "region" {
  type        = string
  description = ""
  default     = ""
}

variable "runtime" {
  type        = string
  description = ""
  default     = "python3.9"
}

variable "lambda_name_consumer" {
  type        = string
  description = ""
  default     = ""
}
variable "lambda_name_publisher" {
  type        = string
  description = ""
  default     = ""
}