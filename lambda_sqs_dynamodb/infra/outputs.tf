output "lambda_function_name" {
  value = aws_lambda_function.sqs_lambda_dynamodb_function.function_name
}

output "lambda_function_arn" {
  value = aws_lambda_function.sqs_lambda_dynamodb_function.arn
}

output "cloudwatch_log_group" {
  value = aws_cloudwatch_log_group.sqs_lambda_dynamodb_loggroup.name
}

# output "aws_lambda_event_source_mapping_name" {
#   value = aws_lambda_event_source_mapping.sqs_lambda_sourcemapping.uuid
# }
