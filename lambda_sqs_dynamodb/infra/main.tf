

# CloudWatch Log group to store Lambda logs
resource "aws_cloudwatch_log_group" "sqs_lambda_dynamodb_loggroup" {
  name              = "/aws/lambda/${var.function_name}"
  retention_in_days = 7
  tags = var.tags
}

resource "aws_lambda_event_source_mapping" "sqs_lambda_demo_sourcemapping" {
  event_source_arn = var.SQSqueueArn
  function_name    = var.function_name
  depends_on = [
    aws_lambda_function.sqs_lambda_dynamodb_function
  ]
}

resource "aws_lambda_function" "sqs_lambda_dynamodb_function" {
  function_name    = var.function_name
  filename         = data.archive_file.lambda_zip_file.output_path
  source_code_hash = filebase64sha256(data.archive_file.lambda_zip_file.output_path)
  role             = aws_iam_role.sqs_lambda_dynamodb_functionrole.arn
  handler          = var.handler
  runtime          = var.runtime
  # layers           = ["arn:aws:lambda:${data.aws_region.current.name}:017000801446:layer:AWSLambdaPowertoolsPython:13"]
  environment {
    variables = {
      DDB_TABLE               = var.dynamodb_table
    }
  }
  depends_on = [aws_cloudwatch_log_group.sqs_lambda_dynamodb_loggroup]
}

