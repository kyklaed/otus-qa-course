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
def add_products(driver):
    page.ProductsPage(driver).steps_to_create_product("nokia", "nokia", "device", "nokia n97")

@pytest.fixture(scope="function")
def check_success(driver):
    page.ProductsPage(driver).check_success()

@pytest.fixture(scope="function")
def edit_product(driver):
    page.ProductsPage(driver).steps_to_edit_product("LOKILA")

@pytest.fixture(scope="function")
def del_products(driver):
    page.ProductsPage(driver).steps_to_del_product()


@pytest.mark.usefixtures("login")
@pytest.mark.usefixtures("login_page")
@pytest.mark.usefixtures("open_login_page")
class TestAddProducts:
    @pytest.mark.usefixtures("add_products")
    def test_add_products(self):
        assert True

    @pytest.mark.usefixtures("check_success")
    def test_check_success_add(self):
        assert True

    @pytest.mark.usefixtures("edit_product")
    def test_edit_product(self):
        assert True

    @pytest.mark.usefixtures("check_success")
    def test_check_success_edit(self):
        assert True

    @pytest.mark.usefixtures("del_products")
    def test_edit_product(self, driver):
        alert = driver.switch_to.alert
        alert.accept()
        assert True

    @pytest.mark.usefixtures("check_success")
    def test_check_success_del(self):
        assert True

