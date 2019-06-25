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
def download_img(driver):
    try:
        page.DownloadPage(driver).upload_img()
    except Exception as err:
        print("error!  = ", err)
        return False
    return True


@pytest.mark.usefixtures("login")
@pytest.mark.usefixtures("login_page")
@pytest.mark.usefixtures("open_login_page")
class TestDBMarketing:
    @pytest.mark.usefixtures("download_img")
    def test_download_img(self, download_img):
        assert download_img

