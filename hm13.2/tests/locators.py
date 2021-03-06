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


class ProductsLocators(object):
    CATALOG = (By.CSS_SELECTOR, 'a[href="#collapse1"]')
    PRODUCTS = (By.CSS_SELECTOR, "ul.in li a[href*=product]")
    ADD_PRODUCTS = (By.CSS_SELECTOR, "div.pull-right a.btn-primary")
    SET_NAME = (By.CSS_SELECTOR, "div.col-sm-10 input[id=input-name1]")
    SET_DESCRIPTION = (By.CSS_SELECTOR, "div.note-editable")
    SET_TAG = (By.CSS_SELECTOR, "input[id=input-meta-title1]")
    CHOOSE_DATA_TREE = (By.CSS_SELECTOR, 'ul.nav-tabs a[href="#tab-data"]')
    CHOOSE_IMAGE_TREE = (By.CSS_SELECTOR, 'ul.nav-tabs a[href="#tab-image"]')
    SET_MODEL = (By.CSS_SELECTOR, "div.col-sm-10 input[id=input-model]")
    SAVE_PRODUCTS = (By.CSS_SELECTOR, "div.pull-right button.btn-primary")
    ALERT = (By.CSS_SELECTOR, "div.alert-success")
    EDIT_BTN = (By.CSS_SELECTOR, 'a[data-original-title="Edit"]')
    SELECT_ALL_CHECKBOX = (By.CSS_SELECTOR, "td.text-center input[onclick]")
    DEL_ALL_PRODUCTS = (By.CSS_SELECTOR, "button.btn-danger")
    OPEN_ADD_IMAGE_MENU = (By.CSS_SELECTOR, 'img[src*="no_image-100x100.png"]')
    ADD_IMAGE = (By.CSS_SELECTOR, 'button[id="button-image"]')
    BTN_UPLOAD_IMAGE = (By.CSS_SELECTOR, 'button[id="button-upload"]')
    SELECT_IMG = (By.CSS_SELECTOR, 'a[href*=".jpg"]')
    ADD_NEW_IMAGE_FOR_PRODUCT = (By.CSS_SELECTOR, 'button[onclick="addImage();"]')


class MarketingLocators(object):
    MENU = (By.CSS_SELECTOR, "li[id='menu-marketing'] a[href='#collapse6']")
    MENU_MARKETING = (By.CSS_SELECTOR, "ul[id='collapse6'] li:first-child a")
    #CAMPAING_NAME = (By.CSS_SELECTOR, "div.table-responsive table tbody tr td:nth-child(2)")
    CAMPAING_NAME = (By.XPATH, "//td[contains(text(), 'HomeWork')]")


class DownloadLocators(object):
    CATALOG = (By.CSS_SELECTOR, 'a[href="#collapse1"]')
    DOWNLOAD = (By.CSS_SELECTOR, "ul.in li a[href*=download]")
    ADD_NEW = (By.CSS_SELECTOR, "div.pull-right a.btn-primary")
    NAME = (By.CSS_SELECTOR, "input.form-control")
    UPLOAD = (By.CSS_SELECTOR, 'button[id="button-upload"]')
    SAVE = (By.CSS_SELECTOR, "div.pull-right button.btn")
    IMG_NAME = (By.XPATH, "//td[contains(text(), 'nokia')]")




