import time

import pytest
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium import webdriver

from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass
from TestData.HomePageData import HomePageData


class TestHomePage(BaseClass):

    def test_formSubmission(self, getData):
        log = self.getLogger()

        homePage = HomePage(self.driver)
        log.info("first name is "+getData["firstname"])
        homePage.getName().send_keys(getData["firstname"])
        homePage.getEmail().send_keys(getData["lastname"])
        homePage.getCheckBox().click()
        self.selectOptionByText(homePage.getGender(), getData["gender"])
        homePage.submitForm().click()
        alertText = homePage.getSuccessMessage().text
        assert ("Success" in alertText)
        self.driver.refresh()

    @pytest.fixture(params=HomePageData.test_HomePage_data)
    def getData(self, request):
        return request.param
