import pytest
import paramiko


def pytest_addoption(parser):
    parser.addoption("--host", action="store", default="192.168.88.242")
    parser.addoption("--port", action="store", default=2222)
    parser.addoption("--user", action="store", default="root")
    parser.addoption("--password", action="store", default="1234567890")


@pytest.fixture(scope="function", autouse="True")
def client(request):
    host = request.config.getoption("--host")
    port = request.config.getoption("--port")
    user = request.config.getoption("--user")
    password = request.config.getoption("--password")
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname=host, username=user, password=password, port=port)
    stdin, stdout, stderr = client.exec_command(request.param)
    data = stdout.read() + stderr.read()
    return data.decode('utf-8')



