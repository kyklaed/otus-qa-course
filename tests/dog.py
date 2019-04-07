import pytest


class TestDogApi:

    def test_code(self, client, test_dog_code):
        url = 'https://dog.ceo/api/breed/{}/images/random'.format(test_dog_code)
        status = client.get(url)
        code = status.status_code
        assert code == 200

    def test_status(self, client, test_dog_status):
        url = 'https://dog.ceo/api/breed/{}/images/random'.format(test_dog_status)
        status = client.get(url)
        code = status.status_code
        json = status.json()
        assert code == 200
        assert json['status'] == "success"

    def test_header(self, client, test_dog_header):
        url = 'https://dog.ceo/api/breed/{}/images/random'.format(test_dog_header[0])
        for n, item in enumerate(test_dog_header[1]):
            status = client.post(url, item)
            code = status.status_code
            assert code == 200
            assert status.headers['Content-type'] in test_dog_header[1]


# a = TestDogApi()
# a.test_code("african")
# a.test_status("african")
# a.test_type("african", "application/json")

