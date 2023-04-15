#Dynamodb
output "dynamodb_arn" {
  # count = var.create_dynamodb ? 1 : 0
  value = aws_dynamodb_table.one[0].arn
}

#mq
# output "mq_broker_arn" {
#   # count = var.create_mq ? 1 : 0
#   value = aws_mq_broker.oneracao[0].arn
# }

#sqs
output "sqs_queue_url" {
  # count = var.create_sqs ? 1 : 0
  value = aws_sqs_queue.sqs_lambda_queue[0].url
}

output "sqs_queue_arn" {
  # count = var.create_sqs ? 1 : 0
  value = aws_sqs_queue.sqs_lambda_queue[0].arn
}