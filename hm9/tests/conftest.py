import pytest
from selenium import webdriver
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener
import logging
import os
import platform


class Handler(AbstractEventListener):
    def __init__(self):
        self.log = ''.join((os.path.abspath(os.curdir), "/screenshots/log.txt"))
        if not os.path.exists(self.log):
            os.makedirs(os.path.abspath(os.curdir))

        open(self.log, 'a', encoding='utf-8')
        os.system(r' >{0}'.format(self.log))

    def write_log(self, string):
        file = open(self.log, 'a', encoding='utf-8')
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
        driver.save_screenshot(''.join((os.path.abspath(os.curdir),"/screenshots/exception.png")))
        print(exception)
        self.write_log("{0}\n".format(exception))


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--url", action="store", default="http://192.168.88.243//")


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

@pytest.mark.usefixtures("environment_info")
@pytest.fixture(scope='session', autouse=True)
def configure_html_report_env(request, environment_info):
    request.config._metadata.update(
        {"browser": request.config.getoption("--browser"),
         "address": request.config.getoption("--url"),
         "os platform": environment_info[0],
         "os": environment_info[1],
         "python v": environment_info[2]})
    yield


@pytest.mark.usefixtures("environment_info")
@pytest.fixture(scope='session', autouse=True)
def extra_json_environment(request, environment_info):
    request.config._json_environment.append(("os platform", environment_info[0]))
    request.config._json_environment.append(("python v", environment_info[2]))


@pytest.fixture(scope="session")
def environment_info():
    os_platform = platform.platform()
    dist = platform.system()
    python = platform.python_version()
    return os_platform, dist, python

