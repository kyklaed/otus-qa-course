import unittest
from unittest.mock import patch, Mock
from req import get_resp


class Tests(unittest.TestCase):
    def test_mock(self):
        mock_get_patcher = patch('req.requests.get')
        mock_get = mock_get_patcher.start()
        mock_get.return_value = Mock(status_code=200, headers="application/json")
        resp = [{"name": "10up-sanitize.css", "version": "11.0.0"}]
        header = "application/json"
        mock_get.return_value.json.return_value = resp
        response = get_resp('https://api.cdnjs.com/libraries/10up-sanitize.css')
        mock_get_patcher.stop()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(header, response.headers)
        self.assertEqual(response.json(), resp)




if __name__ == "__main__":
    unittest.main()