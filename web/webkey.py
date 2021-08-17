from selenium import webdriver
import time


class WebKey:
    # 初始化
    def __init__(self):
        self.driver = webdriver.Chrome

    # 使用那个浏览器打开网页
    def openbrowser(self, br='gc'):
        # 传一个浏览器，默认谷歌
        if br == 'gc':
            self.driver = webdriver.Chrome()
            # 打开谷歌浏览器
        elif br == 'ff':
            self.driver = webdriver.Firefox()
            # 打开火狐浏览器
        elif br == 'ie':
            self.driver = webdriver.Ie()
            # 打开IE浏览器
        else:
            print('输入浏览器暂不支持，请重新输入！')
        self.driver.maximize_window()

        self.driver.implicitly_wait(10)
        # 隐式等待10秒

    # 打开网站
    def geturl(self, url=None):
        self.driver.get(url)

    # 选择元素定位方式
    def __find_ele(self, locator=''):
        ele = None
        self.ele = None
        if locator.startswith('xpath='):
            ele = self.driver.find_element_by_xpath(locator[locator.find('=') + 1])
        elif locator.startswith('id='):
            ele = self.driver.find_element_by_id(locator[locator.find('=') + 1])
        elif locator.startswith('name='):
            ele = self.driver.find_element_by_name(locator[locator.find('=') + 1])
        elif locator.startswith('tag_name='):
            ele = self.driver.find_element_by_tag_name(locator[locator.find('=') + 1])
        elif locator.startswith('class_name='):
            ele = self.driver.find_element_by_class_name(locator[locator.find('=') + 1])
        elif locator.startswith('link_text='):
            ele = self.driver.find_element_by_link_text(locator[locator.find('=') + 1])
        elif locator.startswith('partial_link_text='):
            ele = self.driver.find_element_by_partial_link_text(locator[locator.find('=') + 1])
        elif locator.startswith('css_selector='):
            ele = self.driver.find_element_by_css_selector(locator[locator.find('=') + 1])
        else:
            ele = self.driver.find_element_by_xpath(locator)

        self.ele = ele
        return ele

    def click(self, locator=None):
        ele = self.__find_ele(locator)
        # ele = self.driver.find_elements_by_xpath(locator)
        ele.click()
        # 点击元素

    def input(self, locator=None, value=None):
        ele = self.__find_ele(locator)
        ele.send_keys(value)

    def intoiframe(self, locator=None):
        ele = self.__find_ele(locator)
        self.driver.switch_to.frame(ele)

    def time_sleep(self, t=1):
        t = int(t)
        time.sleep(t)
