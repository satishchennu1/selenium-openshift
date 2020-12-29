import pytest
from selenium import webdriver

class Test_Application_001:

    def test_applicationsearch(self):
        self.driver=webdriver.Chrome(executable_path="Driver\chromedriver.exe")
        self.driver.get("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")
        self.search=self.driver.find_element_by_xpath("//h1[contains(text(),'Admin area demo')]")
        if self.search == "test":
            print("test is passed")
            assert True
        else:
            assert False
            print("test is failed")

