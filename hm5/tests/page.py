from locators import LoginPageLocators, BaseLocators, ForgotPageLocators, ProductsLocators
import time

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def set_username(self, username):
        self.driver.find_element(*LoginPageLocators.USERNAME).send_keys(username)

    def set_password(self, password):
        self.driver.find_element(*LoginPageLocators.PASSWORD).send_keys(password)

    def login_firefox(self):
        self.driver.find_element(*BaseLocators.FIREFOX_BUTTON_LOGIN).click()

    def login_chrome(self):
        self.driver.find_element(*BaseLocators.CHROME_BUTTON_LOGIN).click()

    def check_badlogin(self):
        return self.driver.find_element(*LoginPageLocators.ERROR)


class LogoutPage:
    def __init__(self, driver):
        self.driver = driver

    def logout(self):
        self.driver.find_element(*BaseLocators.LOGOUT_BUTTON).click()


class ForgotPage:
    def __init__(self, driver):
        self.driver = driver

    def find_forgot(self):
        self.driver.find_element(*ForgotPageLocators.URL_FORGOT_PASSWORD).click()

    def find_reset_btn(self):
        self.driver.find_element(*ForgotPageLocators.BTN_FORGOT_PASSWORD).click()

    def find_error_forgot(self):
        return self.driver.find_element(*ForgotPageLocators.ALERT_FORGOT_PASSWORD)


class ProductsPage:
    def __init__(self, driver):
        self.driver = driver

    def catalog(self):
        self.driver.find_element(*ProductsLocators.CATALOG).click()

    def catalog_products(self):
        self.driver.find_element(*ProductsLocators.PRODUCTS).click()

    def add_products(self):
        self.driver.find_element(*ProductsLocators.ADD_PRODUCTS).click()

    def set_name(self, name):
        self.driver.find_element(*ProductsLocators.SET_NAME).send_keys(name)

    def set_description(self, description):
        self.driver.find_element(*ProductsLocators.SET_DESCRIPTION).send_keys(description)

    def set_tag(self, tag):
        self.driver.find_element(*ProductsLocators.SET_TAG).send_keys(tag)

    def choose_data_tree(self):
        self.driver.find_element(*ProductsLocators.CHOOSE_DATA_TREE).click()

    def set_model(self, model):
        self.driver.find_element(*ProductsLocators.SET_MODEL).send_keys(model)

    def save_products(self):
        self.driver.find_element(*ProductsLocators.SAVE_PRODUCTS).click()

    def check_success(self):
        self.driver.find_element(*ProductsLocators.ALERT)

    def edit_button(self):
        self.driver.find_element(*ProductsLocators.EDIT_BTN).click()

    def clear_name(self):
        self.driver.find_element(*ProductsLocators.SET_NAME).clear()

    def select_all_checkbox(self):
        self.driver.find_element(*ProductsLocators.SELECT_ALL_CHECKBOX).click()

    def del_all_products(self):
        self.driver.find_element(*ProductsLocators.DEL_ALL_PRODUCTS).click()

    def steps_to_create_product(self, name, description, tag, model):
        self.catalog()
        time.sleep(0.5)
        self.catalog_products()
        self.add_products()
        self.set_name(name)
        self.set_description(description)
        self.set_tag(tag)
        self.choose_data_tree()
        self.set_model(model)
        self.save_products()

    def steps_to_edit_product(self, name):
        self.edit_button()
        self.clear_name()
        self.set_name(name)
        self.save_products()

    def steps_to_del_product(self):
        self.select_all_checkbox()
        self.del_all_products()
        time.sleep(1)




