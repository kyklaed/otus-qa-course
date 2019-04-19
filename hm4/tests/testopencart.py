import pytest
import page
import time


@pytest.fixture(scope="session")
def open_login_page(driver, request):
    return driver.get(request.config.getoption("--url") + 'admin/')


@pytest.fixture(scope="module")
def login_page(driver):
    return page.LoginPage(driver)


@pytest.fixture(scope="function")
def login(login_page, request):
    login_page.set_username("admin")
    login_page.set_password("admin")
    if request.config.getoption("--browser") == "chrome":
        login_page.login_chrome()
    else:
        login_page.login_firefox()
    time.sleep(10)

@pytest.fixture(scope="function")
def logout(driver):
    page.LogoutPage(driver).logout()

@pytest.fixture(scope="function")
def login_bad(login_page, request):
    login_page.set_username("admin1")
    login_page.set_password("admin1")
    if request.config.getoption("--browser") == "chrome":
        login_page.login_chrome()
    else:
        login_page.login_firefox()
    time.sleep(10)

@pytest.fixture(scope="function")
def check_loginbad(driver):
    return page.LoginPage(driver).check_badlogin()

@pytest.fixture(scope="function")
def check_forgot(driver):
    page.ForgotPage(driver).find_forgot()

# @pytest.fixture(scope="function")
# def check_bnt_reset(driver):
#     page.ForgotPage(driver).find_reset_btn()

@pytest.fixture(scope="function")
def check_reset(driver):
    page.ForgotPage(driver).find_reset_btn()
    page.ForgotPage(driver).find_error_forgot()

@pytest.mark.usefixtures("login_page")
@pytest.mark.usefixtures("open_login_page")
class TestLoginPage:

    @pytest.mark.usefixtures("login")
    def test_login(self, driver):
        print(driver.current_url)
        assert "dashboard" in driver.current_url

    @pytest.mark.usefixtures("logout")
    def test_logout(self, driver):
        print(driver.current_url)
        assert "route=common/login" in driver.current_url

    @pytest.mark.usefixtures("check_loginbad")
    @pytest.mark.usefixtures("open_login_page")
    @pytest.mark.usefixtures("login_bad")
    def test_badlogin(self, check_loginbad):
        assert check_loginbad

    @pytest.mark.usefixtures("check_forgot")
    def test_form_forgot_password(self, driver):
        print(driver.current_url)
        assert "forgotten" in driver.current_url

    @pytest.mark.usefixtures("check_reset")
    def test_find_form_forgot(self):
        assert True

