import pytest
import re
import allure


@pytest.mark.usefixtures()
@pytest.mark.parametrize('client', ['-i'], indirect=True)
def test_count_interfaces(client):
    count_interfaces = 0
    for i in client:
        num = re.findall('^[0-9]+: ', i)
        print(num)
        if len(num) > 0:
            count_interfaces += 1
    if count_interfaces == 3:
        assert True
    else:
        assert False



