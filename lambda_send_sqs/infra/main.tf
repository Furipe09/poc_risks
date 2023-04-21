resource "aws_cloudwatch_log_group" "sqs_lambda_dynamodb_loggroup" {
  name              = "/aws/lambda/${var.function_name}"
  retention_in_days = 7
  tags = var.tags
}
resource "aws_lambda_function" "lambda_function" {
  function_name    = var.function_name
  filename         = data.archive_file.lambda_zip_file.output_path
  source_code_hash = data.archive_file.lambda_zip_file.output_base64sha256
  handler          = var.handler
  role             = aws_iam_role.lambda_iam_role.arn
  runtime          = var.runtime
  # https://awslabs.github.io/aws-lambda-powertools-python/2.13.0/#local-development
  # layers = ["arn:aws:lambda:us-east-1:017000801446:layer:AWSLambdaPowertoolsPythonV2:28", ]
  environment {
    variables = {
      SQSqueueUrl = "https://sqs.us-east-1.amazonaws.com/${data.aws_caller_identity.current.account_id}/${var.SQSqueueUrl}" # var.SQSqueueUrl
    }
  }
}
