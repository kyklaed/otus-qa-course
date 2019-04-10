import pytest
import re

endpoints = ["libraries"]
endpoints2 = ["libraries?search={0}"]
endpoints3 = ["1000hz-bootstrap-validator", "10up-sanitize.css", "16pixels", "3Dmol"]


class TestApi:

    @pytest.mark.parametrize("endpoint", endpoints)
    def test_statuscode(self, client, endpoint):
        status = client.get(endpoint)
        assert status.status_code == 200

    @pytest.mark.parametrize("endpoint3", endpoints3)
    @pytest.mark.parametrize("endpoint2", endpoints2)
    def test_data(self, client, endpoint2, endpoint3):
        url = endpoint2.format(endpoint3)
        print(url)
        status = client.get(url)
        assert status.status_code == 200
        assert len(status.headers['date']) > 0

    @pytest.mark.parametrize("endpoint3", endpoints3)
    @pytest.mark.parametrize("endpoint2", endpoints2)
    def test_head(self, client, endpoint2, endpoint3):
        url = endpoint2.format(endpoint3)
        print(url)
        status = client.get(url)
        assert status.status_code == 200
        assert re.search("application/json", status.headers['Content-type']).group() == "application/json"




