resource "aws_dynamodb_table" "one" {
  count = var.create_dynamodb ? 1 : 0
  name  = var.dynamodb_table
  billing_mode   = var.dynamodb_billing_mode
  read_capacity  = var.dynamodb_read_capacity
  write_capacity = var.dynamodb_write_capacity
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

  tags = var.tags
}
