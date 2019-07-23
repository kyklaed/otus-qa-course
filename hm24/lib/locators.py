from selenium.webdriver.common.by import By


class BaseLocators(object):
    FIREFOX_BUTTON_LOGIN = (By.CLASS_NAME, "btn.btn-primary")
    CHROME_BUTTON_LOGIN = (By.TAG_NAME, "Button")
    LOGOUT_BUTTON = (By.CSS_SELECTOR, ".nav > li:nth-child(2) > a:nth-child(1)")


class LoginPageLocators(object):
    USERNAME = (By.ID, "input-username")
    PASSWORD = (By.ID, "input-password")
    ERROR = (By.CSS_SELECTOR, "div.alert.alert-danger.alert-dismissible")


class ClientPageLocators(object):
    LOGIN_STEP1 = (By.XPATH, "//span[contains(text(), 'My Account')]")
    LOGIN_STEP2 = (By.XPATH, "//a[contains(text(), 'Login')]")
    EMAIL = (By.ID, "input-email")
    PASSWORD = (By.ID, "input-password")
    LOGIN = (By.CSS_SELECTOR, "input.btn-primary")


