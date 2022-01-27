from selenium import webdriver
import time

class Hhangtian_h5():

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.get("http://127.0.0.1/#/firstPage")
        time.sleep(3)
        # self.driver.maximize_window()
        time.sleep(3)

    def login(self,username,password):
        self.driver.find_element_by_xpath("//button[@class='special-btn']").click()
        self.driver.find_element_by_xpath("//input[@placeholder='请输入账号']").send_keys(username)
        self.driver.find_element_by_xpath("//input[@placeholder='请输入密码']").send_keys(password)
        self.driver.find_element_by_xpath("//button[contains(.,'登录')]").click()

if __name__=='__main__':
    h5 = Hhangtian_h5()
    h5.login("name","pwd")