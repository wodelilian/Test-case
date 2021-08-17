import pytest
from selenium import webdriver

def test_login():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get('http://47.108.13.13:6983')
    driver.find_element_by_xpath('//*[@id="userName"]').send_keys('admin')
    driver.find_element_by_xpath('//input[@class="userPwd"]').send_keys("Ycya!@#123")
    driver.find_element_by_xpath('//button[@type="button"').click()


pytest.main(["-s","test_login1.py"])