import pytest
from selenium import webdriver
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener
import logging
import os


class Handler(AbstractEventListener):
    def __init__(self):
        if not os.path.exists(os.path.abspath(os.curdir)+"/screenshots"):
            os.makedirs(os.path.abspath(os.curdir))

        open(os.path.abspath(os.curdir)+"/screenshots/log.txt", 'a', encoding='utf-8')
        os.system(r' >{0}'.format(os.path.abspath(os.curdir)+"/screenshots/log.txt"))

    def write_log(self, string):
        file = open(os.path.abspath(os.curdir) + "/screenshots/log.txt", 'a', encoding='utf-8')
        file.write(string)
        file.close()

    def before_find(self, by, value, driver):
        logging.log(level=10, msg="LOG")
        print(by, value)
        self.write_log("{0} {1}\n".format(by, value))

    def after_find(self, by, value, driver):
        print(by, value, "found")
        self.write_log("{0} {1} found\n".format(by, value))

    def on_exception(self, exception, driver):
        driver.save_screenshot(os.path.abspath(os.curdir)+"/screenshots/exception.png")
        print(exception)
        self.write_log("{0}\n".format(exception))


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--url", action="store", default="http://192.168.43.248/")


@pytest.fixture(scope="session", autouse=True)
def driver(request):
    wd = None
    def_opt = ["--start-halfscreen"]#["--headless"]
    browser = request.config.getoption("--browser")
    if browser == 'chrome':
        options = webdriver.ChromeOptions()
        bin = "/home/kyklaed/Загрузки/chromedriver"
        for argg in def_opt:
            options.add_argument(argg)
        wd = EventFiringWebDriver(webdriver.Chrome(executable_path=bin, chrome_options=options), Handler())
    else:
        options = webdriver.FirefoxOptions()
        bin = "/home/kyklaed/Загрузки/geckodriver"
        for argg in def_opt:
            options.add_argument(argg)
        wd = EventFiringWebDriver(webdriver.Firefox(executable_path=bin, firefox_options=options), Handler())
    yield wd
    wd.quit()