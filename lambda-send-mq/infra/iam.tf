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

resource "aws_iam_policy" "lambda_policy" {
  name_prefix = "lambda_policy"
  path        = "/"
  policy      = data.aws_iam_policy_document.lambda_policy_document.json
  lifecycle {
    create_before_destroy = true
  }
}