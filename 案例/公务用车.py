from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

class Office_car():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.get("http://127.0.0.1/#/login")
        time.sleep(3)

    def h5_login(self,username,pwd):
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[1]/div/div/div/input').send_keys(username)

        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div/div/input').send_keys(pwd)

        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[4]/button').click()
        time.sleep(2)

    def h5_unlogin(self):
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[1]/div/img').click()

        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[6]/ul/li[4]/span').click()

    def h5_car_apply(self):
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[1]').click()#点击申请用车

        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[1]').send_keys(Keys.PAGE_DOWN)

        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[3]/div[3]/div/img').click()#点击选择出车时间

        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[9]/div/div/div[2]/div[3]/ul/li[2]').click()

        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[9]/div/div/div[1]/button[2]').click()#确认用车时间

        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[3]/div[4]/div/img').click()

        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[9]/div/div/div[2]/div[3]/ul/li[2]').click()

        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[9]/div/div/div[2]/div[4]/ul/li[2]').click()

        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[9]/div/div/div[1]/button[2]').click()






a=Office_car()
a.h5_login("name","pwd")




























