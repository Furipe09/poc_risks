data "aws_caller_identity" "current" {}

data "aws_region" "current" {}

data "archive_file" "lambda_zip_file" {
  type        = "zip"
  source_dir  = ".${path.module}/app"
  output_path = "${path.module}/lambda.zip"
}
