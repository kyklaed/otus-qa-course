import pytest
import subprocess


@pytest.fixture(scope="function", autouse="True")
def client(request):
    with subprocess.Popen(["python", "sysinfo.py", request.param], stdout=subprocess.PIPE) as sub:
        content = sub.stdout.read().decode('utf-8').split('\n')
        for i in content:
            print(i)
    return content



