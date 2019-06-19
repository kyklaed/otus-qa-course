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
    login_page.set_username("admin")
    login_page.set_password("admin")
    if request.config.getoption("--browser") == "chrome":
        login_page.login_chrome()
    else:
        login_page.login_firefox()
    time.sleep(5)


@pytest.fixture(scope="function")
def logout(driver):
    page.LogoutPage(driver).logout()


@pytest.fixture(scope="function")
def marketing_db(driver):
    try:
        page.MarketingPage(driver).handler_db()
    except Exception as err:
        print("handler_db = ", err)
        return False
    try:
        page.MarketingPage(driver).main_marketing()
    except Exception as err:
        print("main_marketing = ", err)
        return False
    try:
        page.MarketingPage(driver).inside_marketing()
    except Exception as err:
        print("inside_marketing = ", err)
        return False
    try:
        page.MarketingPage(driver).find_tracking()
    except Exception as err:
        print("find_tracking = ", err)
        return False
    return True


@pytest.mark.usefixtures("login")
@pytest.mark.usefixtures("login_page")
@pytest.mark.usefixtures("open_login_page")
class TestDBMarketing:
    @pytest.mark.usefixtures("marketing_db")
    def test_db_marketing(self, marketing_db):
        assert marketing_db

