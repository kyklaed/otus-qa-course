import pytest


class TestBreweryApi:

    def test_code(self, client):
        url = 'https://api.openbrewerydb.org/breweries'
        status = client.get(url)
        code = status.status_code
        assert code == 200

    def test_status(self, client, test_brewery_status):
        for elem in test_brewery_status:
            url = 'https://api.openbrewerydb.org/breweries?page={0}&per_page={1}'.format(elem[0],
                                                                                         elem[1])
            status = client.get(url)
            code = status.status_code
            json = status.json()
            for item in json:
                assert code == 200
                assert type(item['id']) == int

    def test_state(self, client, test_brewery_state):
        for name in test_brewery_state:
            url = 'https://api.openbrewerydb.org/breweries?by_state={}'.format(name[0])
            status = client.get(url)
            code = status.status_code
            cont = status.json()
            for content in cont:
                assert code == 200
                assert content['state'].upper() == content
