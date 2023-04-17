data "archive_file" "lambda_handler" {
  type        = "zip"
  source_dir  = ".${path.module}/src/"
  output_path = "${path.module}/publisher.zip"
}

# data "archive_file" "layer_basicClient_zip_file" {
#   type        = "zip"
#   source_file = ".${path.module}/src/basicClient.py"
#   output_path = "${path.module}/lambda_layer_basicClient.zip"
# }

# data "archive_file" "lambda_publisher_zip_file" {
#   type        = "zip"
#   source_file = ".${path.module}/src/publisher.py"
#   output_path = "${path.module}/lambda_publisher.zip"
# }

# data "archive_file" "lambda_consumer_zip_file" {
#   type        = "zip"
#   source_file = ".${path.module}/src/consumer.py"
#   output_path = "${path.module}/lambda_consumer.zip"
# }

data "aws_iam_policy" "lambda_basic_execution_role_policy" {
  name = "AWSLambdaBasicExecutionRole"
}

data "aws_iam_policy_document" "lambda_policy_document" {
  statement {

    effect = "Allow"

    actions = [
      "sqs:SendMessage",
      "sqs:GetQueueUrl"
    ]

    resources = [
      "*"
      # aws_sqs_queue.sqs_queue.arn
    ]
  }
}