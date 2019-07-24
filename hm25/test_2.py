import requests
import unittest
from unittest import mock


class CdnjsTest:
    def receive_json(self, url):
        response = requests.get(url)
        print(response)
        return response.json()


class MockResponse:
    def __init__(self, *args):
        self.json_data = args[0]
        self.status_code = args[1]

    def json(self):
        return self.json_data


def mocked_requests_get(*args):
    return MockResponse({"name": "10up-sanitize.css", "version": "11.0.0"}, 200)


class CdnjsTestCase(unittest.TestCase):
    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_1(self, mock_get):
        print("mock_get = ", mock_get)
        obj = CdnjsTest()
        json_data = obj.receive_json('https://api.cdnjs.com/libraries/10up-sanitize.css')
        print(json_data)
        self.assertEqual(json_data, {"name": "10up-sanitize.css", "version": "11.0.0"})


if __name__ == '__main__':
    unittest.main()