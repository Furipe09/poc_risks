resource "aws_dynamodb_table" "one" {
  count = var.create_dynamodb ? 1 : 0
  name  = var.dynamodb_table
  # billing_mode   = "PROVISIONED"
  read_capacity  = 20
  write_capacity = 20
  hash_key       = var.hash_key
  range_key      = var.range_key

  attribute {
    name = var.hash_key
    type = "S"
  }

  attribute {
    name = var.range_key
    type = "S"
  }

}
