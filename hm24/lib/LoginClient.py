from robot.api.deco import keyword
from selenium import webdriver
from locators import ClientPageLocators


class LoginClient(object):
    @keyword(name="WebDriverForClient")
    def driver_client(self):
        wd = None
        def_opt = ["--start-halfscreen"]
        options = webdriver.FirefoxOptions()
        bin = "/home/kyklaed/Загрузки/geckodriver"
        for argg in def_opt:
            options.add_argument(argg)
        self.driver = webdriver.Firefox(executable_path=bin, firefox_options=options)

    @keyword(name="openclient")
    def openclient(self, url):
        self.driver.get(url)

    @keyword(name="my_account")
    def my_account(self):
        self.driver.find_element(*ClientPageLocators.LOGIN_STEP1).click()

    @keyword(name="loginpage")
    def loginpage(self):
        self.driver.find_element(*ClientPageLocators.LOGIN_STEP2).click()

    @keyword(name="set_email")
    def set_email(self, email):
        self.driver.find_element(*ClientPageLocators.EMAIL).send_keys(email)

    @keyword(name="set_password_client")
    def set_password_client(self, password):
        self.driver.find_element(*ClientPageLocators.PASSWORD).send_keys(password)

    @keyword(name="login_btn")
    def login_btn(self):
        self.driver.find_element(*ClientPageLocators.LOGIN).click()

    @keyword(name="close_brw")
    def close_brw(self):
        self.driver.quit()

