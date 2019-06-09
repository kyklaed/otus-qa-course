import pytest
import page
import time


@pytest.fixture(scope="session")
def open_login_page(driver, request):
    return driver.get(request.config.getoption("--url") + 'admin/')


@pytest.fixture(scope="module")
def login_page(driver):
    return page.LoginPage(driver)


@pytest.fixture(scope="module")
def login(login_page, request):
    login_page.set_username("demo")
    login_page.set_password("demo")
    if request.config.getoption("--browser") == "chrome":
        login_page.login_chrome()
    else:
        login_page.login_firefox()
    time.sleep(5)


@pytest.fixture(scope="function")
def dad_choose_menu(driver):
    page.MenuDesing(driver).choose_menu()


@pytest.fixture(scope="function")
def dad_element_down(driver):
    page.MenuDesing(driver).dad_element_down()


@pytest.mark.usefixtures("login")
@pytest.mark.usefixtures("login_page")
@pytest.mark.usefixtures("open_login_page")
class TestDAD:
    @pytest.mark.usefixtures("dad_element_down")
    @pytest.mark.usefixtures("dad_choose_menu")
    def test_choose_menu(self):
        assert True



