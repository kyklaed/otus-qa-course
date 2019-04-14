import pytest
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary



class Application:
    def __init__(self, request, browser_name, url):
        self.browser = browser_name
        self.url = url
        self.def_opt = ["--headless"]
        #self.def_opt = ["--start-fullscreen"]
        self.request = request
        self.wd = None

    def obj(self, opt=None):
        if self.browser == 'chrome':
            options = webdriver.ChromeOptions()
            bin = "/home/kyklaed/Загрузки/chromedriver"
            if opt is not None:
                self.def_opt = opt
            for argg in self.def_opt:
                options.add_argument(argg)
            self.wd = webdriver.Chrome(executable_path=bin, chrome_options=options)
        else:
            options = webdriver.FirefoxOptions()
            bin = "/home/kyklaed/Загрузки/geckodriver"
            if opt is not None:
                self.def_opt = opt
            for argg in self.def_opt:
                options.add_argument(argg)
            self.wd = webdriver.Firefox(executable_path=bin, firefox_options=options)
        return self.wd



def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default=None)
    parser.addoption("--url", action="store", default="http://192.168.88.246/")


@pytest.fixture
def app(request):
    return Application(request, request.config.getoption("--browser"), request.config.getoption("--url"))
