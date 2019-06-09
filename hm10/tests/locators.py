from selenium.webdriver.common.by import By


class BaseLocators(object):
    FIREFOX_BUTTON_LOGIN = (By.CLASS_NAME, "btn.btn-primary")
    CHROME_BUTTON_LOGIN = (By.TAG_NAME, "Button")
    LOGOUT_BUTTON = (By.CSS_SELECTOR, ".nav > li:nth-child(2) > a:nth-child(1)")


class LoginPageLocators(object):
    USERNAME = (By.ID, "input-username")
    PASSWORD = (By.ID, "input-password")
    ERROR = (By.CSS_SELECTOR, "div.alert.alert-danger.alert-dismissible")


class MenuDesingLocators(object):
    MENU_DESING = (By.CSS_SELECTOR, 'ul[id="menu"] li[id="menu-design"]')
    MENU_CONSTRUCTOR = (By.CSS_SELECTOR, 'ul[id="menu"] li[id="menu-design"] li:nth-of-type(2)')#,''ul[id="menu"] li[id="menu-design"] :nth-of-type(2) a')
    #ELEMENT_1 = (By.XPATH, "//span[@class='item-title']/span[contains(text(), 'PC')]")
    ELEMENT_1 = (By.XPATH, "//dt.custommenu-item-handle/span[@class='item-title']/span[contains(text(), 'Компьютеры')]")
    ELEMENT_2 = (By.XPATH, "//dt.custommenu-item-handle/span[@class='item-title']/span[contains(text(), 'Ноутбуки')]")

