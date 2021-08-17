from webkey import WebKey
import time

class Modsize:
    def __init__(self):
        self.web = WebKey()
        self.web.openbrowser()

    def login(self):
        self.web.geturl('http://192.168.0.250:6998/')
        self.web.input('//*[@id="userName"]','admin')
        self.web.input('//input[@class="userPwd"]','123456')
        self.web.click('//button[@type="button"]')

    def search_window(self):
        self.web.intoiframe('//*[@id="myframe"]')
        self.web.click('//*[@id="centent"]/div[5]/i')
        self.web.click("//span[contains(.,'苗圃斑块')]")

    def mod_area(self):
        for c in range(1,66):
            for i in range(1,21):
                time.sleep(1)
                self.web.click("//*[@id=\"datagrid-row-r1-2-{}\"]/td[11]/div/div/div/a[1]".format(i))
                # 依次点击列表中20条数据修改
                time.sleep(2)
                self.web.click('//*[@id=\"facilityAdd\"]/div[1]/div/div/ul[2]/li[1]/input')
                # 点击绘制
                time.sleep(4)
                self.web.click("/html/body/div[6]/div[2]/div/div/div[3]/div/button[2]")

                self.web.click("//*[@id=\"facilityAdd\"]/div[2]/ul/li[2]")
                time.sleep(2)
                try:
                    self.web.click("//*[@id=\"facilityAdd\"]/div[2]/ul/li[1]")
                except:
                    pass
            self.web.click("//*[@id=\"main-content\"]/div/div/div/div/div[2]/div[3]/div/div/div/div[2]/table/tbody/tr/td[10]/a/span/span[2]")


if __name__ == '__main__':
    a = Modsize()
    a.login()
    a.search_window()
    a.mod_area()