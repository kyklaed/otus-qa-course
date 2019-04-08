import pytest
import re


class TestApi1:

    def test_statuscode(self, client):
        status = client.get()
        assert status.status_code == 200

    def test_data(self, client):
        status = client.get()
        assert status.status_code == 200
        assert len(status.headers['date']) > 0

    def test_header(self, client):
        status = client.get()
        assert status.status_code == 200
        assert re.search('application/json', status.headers['Content-type']).group()



