# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

provider "aws" {
  profile = "default"
  region  = "us-east-1"
}

data "aws_caller_identity" "current" {}

data "aws_region" "current" {}

data "archive_file" "lambda_zip_file" {
  type        = "zip"
  source_file = "${path.module}/src/app.py"
  output_path = "${path.module}/lambda.zip"
}

# Role to execute lambda
resource "aws_iam_role" "sqs_lambda_dynamodb_functionrole" {
  name               = "sqs_lambda_dynamodb_functionrole"
  assume_role_policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": "sts:AssumeRole",
      "Principal": {
        "Service": "lambda.amazonaws.com"
      },
      "Effect": "Allow",
      "Sid": ""
    }
  ]
}
EOF
}

# CloudWatch Log group to store Lambda logs
resource "aws_cloudwatch_log_group" "sqs_lambda_dynamodb_loggroup" {
  name              = "/aws/lambda/${aws_lambda_function.sqs_lambda_dynamodb_function.function_name}"
  retention_in_days = 30
}

# Custom policy to read SQS queue and write to CloudWatch Logs with least privileges
resource "aws_iam_policy" "sqs_lambda_dynamodb_lambdapolicy" {
  name        = "sqs-lambda-lambdapolicy"
  path        = "/"
  description = "Policy for sqs to lambda"
  policy      = <<EOF
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Effect": "Allow",
      "Action": [
        "sqs:ReceiveMessage",
        "sqs:DeleteMessage",
        "sqs:GetQueueAttributes"
      ],
      "Resource": "*"
    },
    {
      "Effect": "Allow",
      "Action": [
          "logs:CreateLogGroup",
          "logs:CreateLogStream",
          "logs:PutLogEvents"
      ],
      "Resource": "arn:aws:logs:${data.aws_region.current.name}:${data.aws_caller_identity.current.account_id}:log-group:/aws/lambda/${aws_lambda_function.sqs_lambda_dynamodb_function.function_name}:*:*"
    },
    {
            "Effect": "Allow",
            "Action": [
                "dynamodb:GetItem",
                "dynamodb:PutItem",
                "dynamodb:UpdateItem"
            ],
            "Resource": "arn:aws:dynamodb:*:*:table/${var.dynamodb_table}"
        }
  ]
}
EOF
}

resource "aws_iam_role_policy_attachment" "lambda_policy_attachment" {
  role       = aws_iam_role.sqs_lambda_dynamodb_functionrole.name
  policy_arn = aws_iam_policy.sqs_lambda_dynamodb_lambdapolicy.arn
}

resource "aws_lambda_function" "sqs_lambda_dynamodb_function" {
  function_name    = "SQSLambdaToDynamodb"
  filename         = data.archive_file.lambda_zip_file.output_path
  source_code_hash = filebase64sha256(data.archive_file.lambda_zip_file.output_path)
  role             = aws_iam_role.sqs_lambda_dynamodb_functionrole.arn
  handler          = "app.lambda_handler"
  runtime          = "python3.9"
  layers           = ["arn:aws:lambda:${data.aws_region.current.name}:017000801446:layer:AWSLambdaPowertoolsPython:13"]
  environment {
    variables = {
      POWERTOOLS_SERVICE_NAME = "sqs-lambda-dynamodb"
      DDB_TABLE               = var.dynamodb_table
    }
  }
  # depends_on = [aws_cloudwatch_log_group.sqs_lambda_dynamodb_loggroup]
}

resource "aws_lambda_event_source_mapping" "sqs_lambda_demo_sourcemapping" {
  event_source_arn = var.SQSqueueArn
  function_name    = aws_lambda_function.sqs_lambda_dynamodb_function.function_name
}