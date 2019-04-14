import pytest
# import re
# import json


endpoints = ["api/breeds/image/random", "api/breeds/list/all"]
endpoints2 = ["api/breed/{0}/images/random"]
endpoints3 = ["african", "akita", "chow"]


class TestApi:

    @pytest.mark.parametrize("endpoint", endpoints)
    def test_statuscode(self, client, endpoint):
        status = client.get(endpoint)
        assert status.status_code == 200

    @pytest.mark.parametrize("endpoint", endpoints)
    def test_data(self, client, endpoint):
        status = client.get(endpoint)
        assert status.status_code == 200
        assert len(status.headers['date']) > 0

    @pytest.mark.parametrize("endpoint3", endpoints3)
    @pytest.mark.parametrize("endpoint2", endpoints2)
    def test_head(self, client, endpoint2, endpoint3):
        url = endpoint2.format(endpoint3)
        print(url)
        status = client.get(url)
        assert status.status_code == 200
        assert status.headers['Content-type'] == "application/json"



