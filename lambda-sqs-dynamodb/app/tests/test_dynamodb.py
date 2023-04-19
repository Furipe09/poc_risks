import pytest
from moto import mock_dynamodb2
from src.dynamodb import DynamoDB


@mock_dynamodb2
def test_put_item():
    table_name = 'test_table'
    dynamodb = DynamoDB(table_name)
    dynamodb.table.create(
        KeySchema=[{'AttributeName': 'id', 'KeyType': 'HASH'}],
        AttributeDefinitions=[{'AttributeName': 'id', 'AttributeType': 'S'}]
    )

    item = {
        'id': '1',
        'name': 'Test Name'
    }

    # Test the happy path of put_item
    response = dynamodb.put_item(item)
    assert response['ResponseMetadata']['HTTPStatusCode'] == 200

    # Test put_item raises an exception when there is an error
    with pytest.raises(Exception):
        dynamodb.table.put_item = lambda *args, **kwargs: None
        dynamodb.put_item(item)
