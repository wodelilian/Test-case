import pytest
from selenium import webdriver

def test_login():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get('url')
    driver.find_element_by_xpath('//*[@id="userName"]').send_keys('user')
    driver.find_element_by_xpath('//input[@class="userPwd"]').send_keys("pwd")
    driver.find_element_by_xpath('//button[@type="button"').click()


pytest.main(["-s","test_login1.py"])
