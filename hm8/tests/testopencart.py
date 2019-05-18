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
    obj = page.ProductsPage(driver).create_product("nokia", "nokia", "device", "nokia n97")
    print(obj)
    if obj:
        return True
    else:
        return False


@pytest.fixture(scope="function")
def check_success(driver):
    obj = page.ProductsPage(driver).check_success()
    print(obj)
    if obj:
        return True
    else:
        return False


@pytest.fixture(scope="function")
def edit_product(driver):
    obj = page.ProductsPage(driver).edit_product("LOKILA")
    print(obj)
    if obj:
        return True
    else:
        return False


@pytest.fixture(scope="function")
def del_products(driver):
    obj = page.ProductsPage(driver).del_product()
    print(obj)
    if obj:
        return True
    else:
        return False


@pytest.mark.usefixtures("login")
@pytest.mark.usefixtures("login_page")
@pytest.mark.usefixtures("open_login_page")
class TestAddProducts:
    @pytest.mark.usefixtures("add_products")
    def test_add_products(self, add_products):
        assert add_products

    # @pytest.mark.usefixtures("del_products")
    # def test_del_product(self, driver, del_products):
    #     alert = driver.switch_to.alert
    #     alert.accept()
    #     assert del_products
