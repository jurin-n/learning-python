# -*- coding: utf-8 -*-

from product_code import MyGreatClass
import product_code as sut
import unittest
try:
    from unittest import mock
except ImportError:
    import mock

# This method will be used by the mock to replace requests.get
def mocked_requests_get(*args, **kwargs):
    class MockResponse:
        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.status_code = status_code

        def json(self):
            return self.json_data

    if args[0] == 'http://someurl.com/test.json':
        return MockResponse({"key1": "value1"}, 200)
    else:
        return MockResponse({"key2": "value2"}, 200)

    return MockResponse({}, 404)

# Our test case class
class MyGreatClassTestCase(unittest.TestCase):
    sut = None
    
    def setUp(self):
         self.sut = MyGreatClass()

    # We patch 'requests.get' with our own method. The mock object is passed in to our test case method.
    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_fetch(self, mock_get):
        # Assert requests.get calls
        json_data = self.sut.fetch_json('http://someurl.com/test.json')
        self.assertEqual(json_data, {"key1": "value1"})
        json_data = self.sut.fetch_json('http://someotherurl.com/anothertest.json')
        self.assertEqual(json_data, {"key2": "value2"})

        # We can even assert that our mocked method was called with the right parameters
        self.assertIn(mock.call('http://someurl.com/test.json'), mock_get.call_args_list)
        self.assertIn(mock.call('http://someotherurl.com/anothertest.json'), mock_get.call_args_list)

        self.assertEqual(len(mock_get.call_args_list), 2)

    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_fetch_function(self, mock_get):
        # Assert requests.get calls
        json_data = sut.fetch_json('http://someurl.com/test.json')
        self.assertEqual(json_data, {"key1": "value1"})
        json_data = sut.fetch_json('http://someotherurl.com/anothertest.json')
        self.assertEqual(json_data, {"key2": "value2"})

        # We can even assert that our mocked method was called with the right parameters
        self.assertIn(mock.call('http://someurl.com/test.json'), mock_get.call_args_list)
        self.assertIn(mock.call('http://someotherurl.com/anothertest.json'), mock_get.call_args_list)

        self.assertEqual(len(mock_get.call_args_list), 2)

    #@mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_fetch_function_using_real_requests(self):
        from requests.exceptions import ConnectionError
        with self.assertRaises(ConnectionError):
            json_data = sut.fetch_json('http://someurl.com/test.json')
        with self.assertRaises(ConnectionError):
            json_data = sut.fetch_json('http://someotherurl.com/anothertest.json')

if __name__ == '__main__':
    unittest.main()
