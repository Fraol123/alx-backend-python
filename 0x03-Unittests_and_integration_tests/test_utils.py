#!/usr/bin/env python3
'''
Module to test functions in utils.py
'''
import unittest
from utils import access_nested_map, get_json
from parameterized import parameterized, parameterized_class
from unittest.mock import Mock
from unittest.mock import patch
from requests.exceptions import Timeout


class TestAccessNestedMap(unittest.TestCase):
    '''Test class for AccessNestedMap function'''
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, out):
        '''tests access_nested_map function'''
        self.assertEqual(access_nested_map(nested_map, path), out)

    @parameterized.expand([
        ({}, ("a",), ("KeyError", )),
        ({"a": 1}, ("a", "b"), ("KeyError", )),
    ])
    def test_access_nested_map_exception(self, nested_map, path, out):
        '''test access_nested_map function for wrong inputs'''
        with self.assertRaises(KeyError) as ex:
            access_nested_map(nested_map, path)
            excep = ex.exception
            self.assertEqual(excep.args, ("KeyError", ))


class TestGetJson(unittest.TestCase):
    '''Test calss for get_json()'''
    @parameterized.expand([
        ('http://example.com', {'payload': True}),
        ('http://holberton.io', {'payload': False}),
    ])
    @patch('utils.requests')
    def test_get_json(self, test_url, test_payload, mock_requests):
        '''test function with parametrized input and mocks
           utils.request'''
        mock_requests.json.return_value = test_payload
        mock_requests.get.side_effect = Timeout
        with self.assertRaises(Timeout):
            a = get_json(test_url)
            mock_requests.get.assert_called_once()
            mock_requests.get.assertEqual(a, test_payload)
            mock_requests.get.assert_called_with(test_url)
