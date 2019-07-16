from selenium import webdriver
import pytest


@pytest.fixture
def firefox_browser(request):
    wd = webdriver.Remote(
        'http://192.168.88.243:4444/wd/hub',
        desired_capabilities={"browserName": "firefox"})
    request.addfinalizer(wd.quit)
    return wd


def test_grid(firefox_browser):
    firefox_browser.get("http://www.google.com")
    if not "Google" in firefox_browser.title:
        raise Exception("Unable to load google page!")
    elem = firefox_browser.find_element_by_name("q")
    elem.send_keys("firefox")
    elem.submit()
    print(firefox_browser.title)
