import pytest
from selenium import webdriver



def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--url", action="store", default="http://demo23.opencart.pro/")


@pytest.fixture(scope="session", autouse=True)
def driver(request):
    wd = None
    def_opt = ["--start-halfscreen"]
    browser = request.config.getoption("--browser")
    if browser == 'chrome':
        options = webdriver.ChromeOptions()
        bin = "/home/kyklaed/Загрузки/chromedriver"
        for argg in def_opt:
            options.add_argument(argg)
        wd = webdriver.Chrome(executable_path=bin, chrome_options=options)
    else:
        options = webdriver.FirefoxOptions()
        bin = "/home/kyklaed/Загрузки/geckodriver"
        for argg in def_opt:
            options.add_argument(argg)
        wd = webdriver.Firefox(executable_path=bin, firefox_options=options)
    yield wd
    wd.quit()


