import logging

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

driver = None


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    global driver
    service_obj = ""
    log = logging.getLogger()

    browser_name = request.config.getoption("browser_name")

    if browser_name == "chrome":
        # service_obj = Service("C:\\Users\\edgar.acosta\\webdriver\\chrome110\\chromedriver.exe")
        driver = webdriver.Chrome(executable_path="C:\\Users\\edgar.acosta\\webdriver\\chrome\\chromedriver.exe")
        log.info("Chrome driver")

    elif browser_name == "firefox":
        # service_obj = Service("C:\\Users\\edgar.acosta\\webdriver\\firefox\\geckodriver.exe")
        driver = webdriver.Firefox(executable_path="C:\\Users\\edgar.acosta\\webdriver\\firefox\\geckodriver.exe")
        log.info("Gecko driver")

    elif browser_name == "ie":
        log.info("IE driver")

    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()
