from locators import LoginPageLocators, BaseLocators, ForgotPageLocators


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
