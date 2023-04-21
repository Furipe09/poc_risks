
data "archive_file" "lambda_zip_file" {
  type        = "zip"
  source_dir  = ".${path.module}/src"
  output_path = "${path.module}/lambda.zip"
}

data "aws_iam_policy" "lambda_basic_execution_role_policy" {
  name = "AWSLambdaBasicExecutionRole"
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