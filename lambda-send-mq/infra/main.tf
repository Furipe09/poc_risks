# resource "aws_lambda_layer_version" "lambda_layer_client" {
#   filename   = "lambda_layer.zip"
#   layer_name = "basicClient"

#   compatible_runtimes = [var.runtime]
# }

# resource "aws_lambda_function" "lambda_name_publisher" {
#   function_name    = var.lambda_name_publisher
#   filename         = data.archive_file.lambda_publisher_zip_file.output_path
#   source_code_hash = data.archive_file.lambda_publisher_zip_file.output_base64sha256
#   handler          = "publisher.lambda_handler"
#   role             = aws_iam_role.lambda_iam_role.arn
#   runtime          = var.runtime
#     layers = [    aws_lambda_layer_version.lambda_layer_client.arn, ]
#   environment {
#     variables = {
#       QUEUE_URL = var.queue_url
#     }
#   }
# }

# resource "aws_lambda_function" "lambda_name_consumer" {
#   function_name    = var.lambda_name_consumer
#   filename         = data.archive_file.lambda_consumer_zip_file.output_path
#   source_code_hash = data.archive_file.lambda_consumer_zip_file.output_base64sha256
#   handler          = "consumer.lambda_handler"
#   role             = aws_iam_role.lambda_iam_role.arn
#   runtime          = var.runtime
#     layers = [    aws_lambda_layer_version.lambda_layer_client.arn, ]
#   environment {
#     variables = {
#       QUEUE_URL = var.queue_url
#     }
#   }
# }

resource "aws_lambda_function" "lambda_name_teste" {
  function_name    = var.lambda_name_consumer
  filename         = data.archive_file.lambda_handler.output_path
  source_code_hash = data.archive_file.lambda_handler.output_base64sha256
  handler          = "publisher.lambda_handler"
  role             = aws_iam_role.lambda_iam_role.arn
  runtime          = var.runtime
  # layers = [    aws_lambda_layer_version.lambda_layer_client.arn, ]
  environment {
    variables = {
      QUEUE_URL = var.queue_url
      brokerid  = var.brokerid
      username  = var.username
      password  = var.password
      region    = var.region
    }
  }
  #  source_path = [
  #   {
  #     path = ".${path.module}/source"
  #     commands = [
  #       ":zip",
  #       "cd `mktemp -d`",
  #       "python3.9 -m pip install --no-compile --only-binary=:all: --platform=manylinux2014_x86_64 --target=. -r .${abspath(path.module)}/src/requirements.txt",
  #       ":zip .",
  #     ]
  #   }
  # ]
}