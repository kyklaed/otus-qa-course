from locators import LoginPageLocators, BaseLocators, ForgotPageLocators, ProductsLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, StaleElementReferenceException, ElementClickInterceptedException

import time
import pyautogui


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
        self.list_select_img = None

    def catalog(self):
        try:
            self.driver.find_element(*ProductsLocators.CATALOG).click()
        except NoSuchElementException:
            return False

    def catalog_products(self, delay=1):
        try:
            WebDriverWait(self.driver, delay).until(EC.presence_of_element_located((ProductsLocators.PRODUCTS)))
            self.driver.find_element(*ProductsLocators.PRODUCTS).click()
        except (NoSuchElementException, TimeoutException):
            return False

    def add_products(self):
        try:
            self.driver.find_element(*ProductsLocators.ADD_PRODUCTS).click()
        except NoSuchElementException:
            return False

    def set_name(self, name):
        try:
            self.driver.find_element(*ProductsLocators.SET_NAME).send_keys(name)
        except NoSuchElementException:
            return False

    def set_description(self, description):
        try:
            self.driver.find_element(*ProductsLocators.SET_DESCRIPTION).send_keys(description)
        except NoSuchElementException:
            return False

    def set_tag(self, tag):
        try:
            self.driver.find_element(*ProductsLocators.SET_TAG).send_keys(tag)
        except NoSuchElementException:
            return False

    def choose_data_tree(self):
        try:
            self.driver.find_element(*ProductsLocators.CHOOSE_DATA_TREE).click()
        except NoSuchElementException:
            return False

    def set_model(self, model):
        try:
            self.driver.find_element(*ProductsLocators.SET_MODEL).send_keys(model)
        except NoSuchElementException:
            return False

    def save_products(self):
        try:
            self.driver.find_element(*ProductsLocators.SAVE_PRODUCTS).click()
        except NoSuchElementException:
            return False

    def check_success(self):
        try:
            self.driver.find_element(*ProductsLocators.ALERT)
            return True
        except NoSuchElementException:
            return False

    def edit_button(self):
        try:
            self.driver.find_element(*ProductsLocators.EDIT_BTN).click()
        except NoSuchElementException:
            return False

    def clear_name(self):
        try:
            self.driver.find_element(*ProductsLocators.SET_NAME).clear()
        except NoSuchElementException:
            return False

    def select_all_checkbox(self):
        try:
            self.driver.find_element(*ProductsLocators.SELECT_ALL_CHECKBOX).click()
        except NoSuchElementException:
            return False

    def del_all_products(self):
        try:
            self.driver.find_element(*ProductsLocators.DEL_ALL_PRODUCTS).click()
        except NoSuchElementException:
            return False

    def choose_image_tree(self):
        try:
            self.driver.find_element(*ProductsLocators.CHOOSE_IMAGE_TREE).click()
        except NoSuchElementException:
            return False

    def create_images_for_prod(self, count_img=2):
        try:
            for i in range(count_img):
                self.driver.find_element(*ProductsLocators.ADD_NEW_IMAGE_FOR_PRODUCT).click()
        except NoSuchElementException:
            return False

    def download_img(self):
        time.sleep(1)
        self.driver.find_element(*ProductsLocators.ADD_IMAGE).click()
        time.sleep(1)
        self.driver.find_element(*ProductsLocators.BTN_UPLOAD_IMAGE).click()
        self.choose_image()
        time.sleep(2)
        self.click_alert()

    def click_img_for_choose(self, num):
        try:
            self.list_select_img = self.driver.find_elements(*ProductsLocators.SELECT_IMG)
            self.list_select_img[num].click()
        except (StaleElementReferenceException, ElementClickInterceptedException) as err:
            print(err)

    def add_image(self):
        try:
            open_add_img_menu = self.driver.find_elements(*ProductsLocators.OPEN_ADD_IMAGE_MENU)
            for num, element in enumerate(open_add_img_menu):
                time.sleep(5)
                print(num, element)
                if num == 0:
                    print(element)
                    element.click()
                    self.download_img()
                    self.click_img_for_choose(num)
                else:
                    print(element)
                    element.click()
                    time.sleep(5)
                    self.driver.find_element(*ProductsLocators.ADD_IMAGE).click()
                    time.sleep(5)
                    self.click_img_for_choose(num)
            time.sleep(5)

        except NoSuchElementException:
            return False

    def choose_image(self, img=2):
        if self.driver.__dict__['capabilities']['browserName'] == 'chrome':
            for i in range(6):
                pyautogui.press("tab")
            time.sleep(2)
            pyautogui.press('enter')
            time.sleep(2)
            for i in range(3):
                pyautogui.press("right")
            pyautogui.press("down")

            pyautogui.keyDown("shift")
            for i in range(img):
                pyautogui.press("down")
            pyautogui.keyUp('shift')
            time.sleep(2)
            pyautogui.press('enter')

        else:
            pyautogui.keyDown("shift")
            for i in range(img):
                pyautogui.press("down")
            pyautogui.keyUp('shift')
            time.sleep(2)
            pyautogui.press('enter')

    def click_alert(self):
        alert = self.driver.switch_to.alert
        alert.accept()

    def create_product(self, name, description, tag, model):
        self.catalog()
        self.catalog_products()
        self.add_products()
        self.set_name(name)
        self.set_description(description)
        self.set_tag(tag)
        self.choose_data_tree()
        self.set_model(model)
        self.choose_image_tree()
        self.create_images_for_prod()
        self.add_image()
        self.save_products()
        return True

    def edit_product(self, name):
        self.edit_button()
        self.clear_name()
        self.set_name(name)
        self.save_products()
        return True

    def del_product(self):
        self.select_all_checkbox()
        self.del_all_products()
        time.sleep(1)
        return True




