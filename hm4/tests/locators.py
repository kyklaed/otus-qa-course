from selenium.webdriver.common.by import By


class BaseLocators(object):
    FIREFOX_BUTTON_LOGIN = (By.CLASS_NAME, "btn.btn-primary")
    CHROME_BUTTON_LOGIN = (By.TAG_NAME, "Button")
    LOGOUT_BUTTON = (By.CSS_SELECTOR, ".nav > li:nth-child(2) > a:nth-child(1)")


class LoginPageLocators(object):
    USERNAME = (By.ID, "input-username")
    PASSWORD = (By.ID, "input-password")
    ERROR = (By.CSS_SELECTOR, "div.alert.alert-danger.alert-dismissible")

class ForgotPageLocators(object):
    URL_FORGOT_PASSWORD = (By.CSS_SELECTOR, "span.help-block > a[href]")
    BTN_FORGOT_PASSWORD = (By.CSS_SELECTOR, "form[method=post] div button")
    ALERT_FORGOT_PASSWORD = (By.CSS_SELECTOR, "div.alert-dismissible")
