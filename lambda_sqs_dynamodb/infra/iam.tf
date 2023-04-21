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
