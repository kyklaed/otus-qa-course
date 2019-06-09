from locators import LoginPageLocators, BaseLocators, MenuDesingLocators
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
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


class MenuDesing:
    def __init__(self, driver):
        self.driver = driver

    def choose_menu(self, delay=5):
        try:
            WebDriverWait(self.driver, delay).until(EC.presence_of_element_located((MenuDesingLocators.MENU_DESING)))
            MENU_DESING = self.driver.find_element(*MenuDesingLocators.MENU_DESING)
            ActionChains(self.driver).move_to_element(MENU_DESING).perform()

            WebDriverWait(self.driver, delay).until(EC.presence_of_element_located((MenuDesingLocators.MENU_CONSTRUCTOR)))
            #MENU_CONSTRUCTOR = self.driver.find_element(*MenuDesingLocators.MENU_CONSTRUCTOR)
            self.driver.find_element(*MenuDesingLocators.MENU_CONSTRUCTOR).click()
            #ActionChains(self.driver).move_to_element(MENU_CONSTRUCTOR).click(MENU_CONSTRUCTOR).perform()
            time.sleep(5)
            return True
        except (NoSuchElementException, TimeoutException):
            return False

    def element_1(self, delay=5):
        try:
            WebDriverWait(self.driver, delay).until(EC.presence_of_element_located((MenuDesingLocators.ELEMENT_1)))
            return self.driver.find_element(*MenuDesingLocators.ELEMENT_1)
        except (NoSuchElementException, TimeoutException):
            return False

    def element_2(self, delay=5):
        try:
            WebDriverWait(self.driver, delay).until(EC.presence_of_element_located((MenuDesingLocators.ELEMENT_2)))
            return self.driver.find_element(*MenuDesingLocators.ELEMENT_2)
        except (NoSuchElementException, TimeoutException):
            return False

    def dad_element_down(self):
        try:
            elem1 = self.element_1()
            #self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            elem2 = self.element_2()
            time.sleep(2)
            ActionChains(self.driver).drag_and_drop(elem1, elem2).perform()
            time.sleep(2)
            return True
        except NoSuchElementException:
            return False




