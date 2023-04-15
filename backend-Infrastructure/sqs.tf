
resource "aws_sqs_queue" "sqs_lambda_queue" {
  count = var.create_sqs ? 1 : 0
  name  = var.sqs_lambda
}
