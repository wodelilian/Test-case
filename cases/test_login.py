class Test_Login():
    def setup(self):
        from selenium import webdriver
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)



    def teardown(self):
        print("用例执行结束")


    def test_login(self):
        self.driver.get('http://47.108.13.13:6983')
        self.driver.find_element_by_xpath('//*[@id="userName"]').send_keys('admin')
        self.driver.find_element_by_xpath('//input[@class="userPwd"]').send_keys("Ycya!@#123")
        self.driver.find_element_by_xpath('//button[@type="button"')

