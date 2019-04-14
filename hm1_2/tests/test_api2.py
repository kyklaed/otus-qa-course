import pytest
import re


@pytest.mark.parametrize("code", [200])
@pytest.mark.usefixtures("client2")
def test_statuscode(client2, code):
    status = client2.get()
    assert status.status_code == code


@pytest.mark.parametrize("code", [200])
@pytest.mark.usefixtures("client2")
def test_data(client2, code):
    status = client2.get()
    assert status.status_code == code
    assert len(status.headers['date']) > 0


@pytest.mark.parametrize("code", [200])
@pytest.mark.usefixtures("client2")
def test_header(client2, code):
    status = client2.get()
    assert status.status_code == code
    assert re.search(client2.head['Content-type'], status.headers['Content-type']).group()


