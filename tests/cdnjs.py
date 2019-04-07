import pytest
import re


class TestCDNApi:

    def test_code(self, client):
        url = 'https://api.cdnjs.com/libraries'
        status = client.get(url)
        code = status.status_code
        assert code == 200

    def test_len_total(self, client):
        url = 'https://api.cdnjs.com/libraries'
        status = client.get(url)
        code = status.status_code
        json = status.json()
        assert code == 200
        assert json['total'] == len(json['results'])

    def test_header(self, client, test_header):
        for item in test_header:
            url = 'https://api.cdnjs.com/libraries?search={}'.format(item[0])
            status = client.get(url, item[1])
            code = status.status_code
            math = re.match(item[1], status.headers['content-type'])
            assert code == 200
            assert math is not None
            assert item[1] == math.group()
