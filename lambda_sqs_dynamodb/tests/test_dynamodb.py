import unittest
import logging
from unittest.mock import MagicMock
from botocore.exceptions import ClientError
import os
import sys
import json
sys.path.insert(1, '../app')
import dynamodb

logging.basicConfig(level=logging.INFO)


class TestDynamoDB(unittest.TestCase):
    def setUp(self):
        self.table_name = 'approvedRisk'
        self.dynamodb = dynamodb.DynamoDB(self.table_name)

    def test_put_item(self):
        mock_table = MagicMock()
        # mock_response = {"ResponseMetadata": {"HTTPStatusCode": 200}}
        item = {"IdTransacao": "99",  "IdCliente": "99", "name": "John Does"}
        mock_response = item
        mock_table.put_item.return_value = mock_response
        self.dynamodb.table = mock_table

        response = self.dynamodb.put_item(item)

        mock_table.put_item.assert_called_once_with(Item=item)
        self.assertEqual(response, mock_response)
        # logging.info.assert_any_call(f"Item inserido na tabela {self.table_name}: {mock_response}")
        logging.info(f"## Item inserido na tabela {self.table_name}: {mock_response}")

    def test_put_item_error(self):
        mock_table = MagicMock()
        mock_error = ClientError({"Error": {"Code": "Error"}}, "operation_name")
        mock_table.put_item.side_effect = mock_error
        self.dynamodb.table = mock_table

        item = {"key": "value"}

        with self.assertRaises(ClientError):
            self.dynamodb.put_item(item)

        mock_table.put_item.assert_called_once_with(Item=item)
        # logging.error.assert_any_call(f"Erro ao inserir item na tabela {self.table_name}: {mock_error}")
        logging.error(f"Erro ao inserir item na tabela {self.table_name}: {mock_error}")
