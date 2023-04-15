output "QueuePublisherFunction" {
  value       = aws_lambda_function.lambda_function.arn
  description = "QueuePublisherFunction function name"
}