from robot.api.deco import keyword
from selenium import webdriver
from locators import LoginPageLocators, BaseLocators


class LoginAdmin(object):
    @keyword(name="WebDriverForAdmin")
    def driver(self):
        wd = None
        def_opt = ["--start-halfscreen"]
        options = webdriver.FirefoxOptions()
        bin = "/home/kyklaed/Загрузки/geckodriver"
        for argg in def_opt:
            options.add_argument(argg)
        self.driver = webdriver.Firefox(executable_path=bin, firefox_options=options)

    @keyword(name="open")
    def open(self, url):
        self.driver.get(url)

    @keyword(name="set_username")
    def set_username(self, username):
        self.driver.find_element(*LoginPageLocators.USERNAME).send_keys(username)

    @keyword(name="set_password")
    def set_password(self, password):
        self.driver.find_element(*LoginPageLocators.PASSWORD).send_keys(password)

    @keyword(name="loginTO")
    def login(self):
        self.driver.find_element(*BaseLocators.FIREFOX_BUTTON_LOGIN).click()

    @keyword(name="close")
    def close(self):
        self.driver.quit()

