class Test_Login():
    def setup(self):
        from selenium import webdriver
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)



    def teardown(self):
        print("用例执行结束")


    def test_login(self):
        self.driver.get('url')
        self.driver.find_element_by_xpath('//*[@id="userName"]').send_keys('user')
        self.driver.find_element_by_xpath('//input[@class="userPwd"]').send_keys("pwd")
        self.driver.find_element_by_xpath('//button[@type="button"')
