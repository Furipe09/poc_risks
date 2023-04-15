output "lambda_function_name" {
  value = aws_lambda_function.sqs_lambda_dynamodb_function.function_name
}

output "cloudwatch_log_group" {
  value = aws_cloudwatch_log_group.sqs_lambda_dynamodb_loggroup.name
}