import pytest


@pytest.mark.parametrize('client', ['service nginx status'], indirect=True)
def test_status_before_stop(client):
    find = client.find("running")
    if find > -1:
        assert True
    else:
        assert False


@pytest.mark.parametrize('client', ['service nginx stop'], indirect=True)
def test_stop(client):
    assert True


@pytest.mark.parametrize('client', ['service nginx status'], indirect=True)
def test_status_after_stop(client):
    find = client.find("dead")
    if find > -1:
        assert True
    else:
        assert False


@pytest.mark.parametrize('client', ['service nginx start'], indirect=True)
def test_status_start(client):
    assert True


@pytest.mark.parametrize('client', ['service nginx status'], indirect=True)
def test_status_after_start(client):
    find = client.find("running")
    if find > -1:
        assert True
    else:
        assert False


