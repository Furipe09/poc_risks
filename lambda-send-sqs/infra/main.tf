provider "aws" {
  profile = "default"
  region  = "us-east-1"
}

resource "aws_lambda_function" "lambda_function" {
  function_name    = "LambdaToSQSFunction"
  filename         = data.archive_file.lambda_zip_file.output_path
  source_code_hash = data.archive_file.lambda_zip_file.output_base64sha256
  handler          = "app.lambda_handler"
  role             = aws_iam_role.lambda_iam_role.arn
  runtime          = "python3.9"
  environment {
    variables = {
      SQSqueueUrl = var.SQSqueueUrl
    }
  }
}

data "archive_file" "lambda_zip_file" {
  type        = "zip"
  source_file = ".${path.module}/source/app.py"
  output_path = "${path.module}/lambda.zip"
}

data "aws_iam_policy" "lambda_basic_execution_role_policy" {
  name = "AWSLambdaBasicExecutionRole"
}

resource "aws_iam_role" "lambda_iam_role" {
  name_prefix = "RoleLambdaSQS-"
  managed_policy_arns = [
    data.aws_iam_policy.lambda_basic_execution_role_policy.arn,
    aws_iam_policy.lambda_policy.arn
  ]

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

data "aws_iam_policy_document" "lambda_policy_document" {
  statement {

    effect = "Allow"

    actions = [
      "sqs:SendMessage*"
    ]

    resources = [
      "*"
      # aws_sqs_queue.sqs_queue.arn
    ]
  }
}

resource "aws_iam_policy" "lambda_policy" {
  name_prefix = "lambda_policy"
  path        = "/"
  policy      = data.aws_iam_policy_document.lambda_policy_document.json
  lifecycle {
    create_before_destroy = true
  }
}


