import time
from appium import webdriver
import random
from selenium.webdriver.common.touch_actions import TouchActions

class Gongwuyongche():
    def __init__(self):
        desired_caps = {
            "deviceName": "iphone",#测试设备名称

            "appPackage": "app-name",#测试软件包名

            "appActivity": "start-page",#测试软件启动界面

            "platformName": "Android",#自动化测试平台

            "platformVersion": "9",#测试的版本

            "unicodeKeyboard": True,#输入带有中文必备条件
            "resetKeyboard": True}#清空输入
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)
        try:
            self.driver.find_element_by_id("android:id/button1").click()#app获取权限弹窗
            time.sleep(1)
            self.driver.find_element_by_id("android:id/button1").click()#app获取权限弹窗
        except:
            pass

    def move_screen(self, start_x_percentage, start_y_percentage, end_x_percentage, end_y_percentage):
        screen_size = self.driver.get_window_size()#获取屏幕总像素(1080,2028)
        start_x = screen_size['width'] * float(start_x_percentage)#元素最初的X坐标  start_xpercentage是元素坐标在总像素中的占比   (宽度总像素1080/当前X的坐标）
        start_y = screen_size['height'] * float(start_y_percentage)#元素最初的Y坐标
        end_x = screen_size['width'] * float(end_x_percentage)#元素最终的X坐标
        end_y = screen_size['height'] * float(end_y_percentage)#元素最终的Y坐标
        time.sleep(2)
        self.driver.swipe(start_x, start_y, end_x, end_y, duration=500)

    def login(self,username):
        self.driver.find_element_by_id("login_name_edit").send_keys(username)#输入账户名

        self.driver.find_element_by_id("login_password_edit").send_keys("pwd")#输入密码

        self.driver.find_element_by_id("login_button").click()#点击登陆
        time.sleep(2)
        try:
            self.driver.find_element_by_id("android:id/button1").click()#app获取权限弹窗
        except:
            pass


    def apply_car_layout(self):

        self.driver.find_element_by_id("apply_car_layout").click()#点击用车申请

        usecar_name = "张三"+str(random.randint(1,9527))

        self.driver.find_element_by_id("take_car_name").send_keys(usecar_name)#输入乘车人

        usecar_phone = "138" + str(random.randint(11111111, 99999999))

        self.driver.find_element_by_id("take_car_number").send_keys(usecar_phone)#输入联系电话

        usecar_num=random.randint(1,9)#导入随机数

        self.driver.find_element_by_id("user_car_person_count").send_keys(usecar_num)#随机输入1-9人

        self.driver.find_element_by_id("start_time_text").click()#点击开始时间
        # time.sleep(2)

        self.move_screen("0.53","0.71","0.53","0.56")

        #选择开始时间
        # screen_size = self.driver.get_window_size()
        # start_x = screen_size['width'] * 0.53
        # start_y = screen_size['height'] * 0.71
        # end_x = screen_size['width'] * 0.53
        # end_y = screen_size['height'] * 0.56
        # time.sleep(2)
        # self.driver.swipe(start_x,start_y,end_x,end_y, duration=500)#开始滑动屏幕，500毫秒内完成

        # TouchActions().press(x=577, y=1313).move_to(x=580, y=1176).release().perform()
        time.sleep(2)
        self.driver.find_element_by_id("android:id/button1").click()#确定开始时间

        self.driver.find_element_by_id("end_time_text").click()#选择结束时间

        #选择结束时间
        time.sleep(2)

        self.move_screen("0.53","0.71","0.53","0.56")

        self.move_screen("0.68","0.64","0.68","0.57")

        # screen_size = self.driver.get_window_size()
        # start_x1 = screen_size['width'] * 0.53
        # start_y1 = screen_size['height'] * 0.71
        # end_x1 = screen_size['width'] * 0.53
        # end_y1 = screen_size['height'] * 0.56
        # time.sleep(2)
        # self.driver.swipe(start_x1,start_y1,end_x1,end_y1, duration=500)
        # start_x2 = screen_size['width'] * 0.68
        # start_y2 = screen_size['height'] * 0.64
        # end_x2 = screen_size['width'] * 0.68
        # end_y2 = screen_size['height'] * 0.57
        # time.sleep(2)
        # self.driver.swipe(start_x2, start_y2, end_x2, end_y2, duration=500)

        time.sleep(1)
        self.driver.find_element_by_id("android:id/button1").click()#确认结束时间

        self.move_screen("0.69","0.85","0.69","0.55")

        #滑动屏幕至底部
        # screen_size = self.driver.get_window_size()
        # start_x2 = screen_size['width'] * 0.69
        # start_y2 = screen_size['height'] * 0.85
        # end_x2 = screen_size['width'] * 0.69
        # end_y2 = screen_size['height'] * 0.55
        # time.sleep(2)
        # self.driver.swipe(start_x2,start_y2,end_x2,end_y2, duration=500)

        self.driver.find_element_by_id("need_car_type_sp").click()#点击车辆类型

        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[2]/android.widget.ImageView[2]").click()
        #添加用车数量

        self.driver.find_element_by_id("com.hangtian.offcialvehicles:id/confirmBtn").click()#确认用车数量

        self.driver.find_element_by_id("com.hangtian.offcialvehicles:id/route_sp").click()
        #选择用车路线

        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.TextView[3]").click()
        #确认用车路线

        self.driver.find_element_by_id("com.hangtian.offcialvehicles:id/confirm_btn").click()
        #确认新增订单


    def my_apply_car_layout(self):
        self.driver.find_element_by_id("com.hangtian.offcialvehicles:id/my_apply_car_layout").click()#点击我的用车
        time.sleep(2)
        新增用车申请 = time.strftime("%Y_%m_%d_%H_%M_%S") + ".png"
        self.driver.save_screenshot("D:\\公务用车\\新增用车申请" + 新增用车申请)
        #截图保存最新的订单
        self.driver.find_element_by_accessibility_id("转到上一层级").click()
        #返回主页面

    def unlogin(self):
        #退出登录
        self.driver.find_element_by_id("com.hangtian.offcialvehicles:id/main_more_img").click()


        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v4.widget.DrawerLayout/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.support.v7.widget.LinearLayoutCompat[5]/android.widget.CheckedTextView").click()


        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView[2]").click()

    def car_check_layout(self):
        self.driver.find_element_by_id("com.hangtian.offcialvehicles:id/radiobutton_check").click()#进入审批页面

        self.driver.find_element_by_id("com.hangtian.offcialvehicles:id/car_check_layout").click()#点击用车审批

        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.support.v4.view.ViewPager/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.RelativeLayout").click()

        self.move_screen("0.46","0.85","0.46","0.49")

        # screen_size = self.driver.get_window_size()
        # start_x3 = screen_size['width'] * 0.46
        # start_y3 = screen_size['height'] * 0.85
        # end_x3 = screen_size['width'] * 0.46
        # end_y3 = screen_size['height'] * 0.49
        # time.sleep(2)
        # self.driver.swipe(start_x3, start_y3, end_x3, end_y3, duration=500)
        #屏幕下滑

        self.driver.find_element_by_id("com.hangtian.offcialvehicles:id/ok_button").click()#点击通过

        self.driver.find_element_by_id("android:id/button1").click()#确认审批通过

        self.driver.find_element_by_accessibility_id("转到上一层级").click()#返回审批主页面


    def scheduling_layout(self):
        self.driver.find_element_by_id("com.hangtian.offcialvehicles:id/radiobutton_scheduling").click()#进入派车页面

        self.driver.find_element_by_id("com.hangtian.offcialvehicles:id/scheduling_layout").click()#点击我的调度

        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.support.v4.view.ViewPager/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.RelativeLayout").click()
        #选择第一个订单进行调度

        self.move_screen("0.37","0.90","0.37","0.23")

        # screen_size = self.driver.get_window_size()
        # start_x = screen_size['width'] * 0.37
        # start_y = screen_size['height'] * 0.90
        # end_x = screen_size['width'] * 0.37
        # end_y = screen_size['height'] * 0.23
        # time.sleep(2)
        # self.driver.swipe(start_x, start_y, end_x, end_y, duration=500)
        #屏幕下滑

        self.driver.find_element_by_id("com.hangtian.offcialvehicles:id/show_dispatch_dep").click()#选择车队

        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.TextView[2]").click()
        #选择第二个车队

        self.driver.find_element_by_id("com.hangtian.offcialvehicles:id/share_car_btn").click()#点击确认

        self.driver.find_element_by_id("com.hangtian.offcialvehicles:id/confirm_button").click()#确认调度

        self.driver.find_element_by_accessibility_id("转到上一层级").click()#返回派车主页面

    def sent_layout(self):
        try:
            self.driver.find_element_by_id("com.hangtian.offcialvehicles:id/radiobutton_scheduling").click()  # 进入派车页面
        except:
            pass

        self.driver.find_element_by_id("com.hangtian.offcialvehicles:id/sent_layout").click()#进入派车订单页面

        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.support.v4.view.ViewPager/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.RelativeLayout").click()
        # 选择第一个订单

        self.move_screen("0.38","0.97","0.38","0.46")

        # screen_size = self.driver.get_window_size()
        # start_x = screen_size['width'] * 0.38
        # start_y = screen_size['height'] * 0.97
        # end_x = screen_size['width'] * 0.38
        # end_y = screen_size['height'] * 0.46
        # time.sleep(2)
        # self.driver.swipe(start_x, start_y, end_x, end_y, duration=500)

        self.driver.find_element_by_id("com.hangtian.offcialvehicles:id/cancel_button").click()#点击派车

        self.driver.find_element_by_id("com.hangtian.offcialvehicles:id/bt_add").click()#点击添加

        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ListView/android.widget.LinearLayout[1]").click()
        # 选择车辆

        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ListView/android.widget.LinearLayout[1]").click()
        #选择司机

        self.driver.find_element_by_id("com.hangtian.offcialvehicles:id/bt_confirm").click()#确认添加司机
        time.sleep(2)

        self.driver.find_element_by_accessibility_id("转到上一层级").click()#返回派车主页面



    def rentrun_layout(self):
        self.driver.find_element_by_id("com.hangtian.offcialvehicles:id/radiobutton_scheduling").click()#点击底部派车按钮

        self.driver.find_element_by_id("com.hangtian.offcialvehicles:id/rentrun_layout").click()#点击归队登记

        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.support.v4.view.ViewPager/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[1]").click()
        # 选择第一个订单进行归队

        start_road_code=random.randint(1,9)#导入随机函1-9设为起始路码

        end_road_code=random.randint(10,15)#导入随机函10-15设为终止路码

        self.driver.find_element_by_id("com.hangtian.offcialvehicles:id/start_road_code_text").send_keys(start_road_code)#输入起始路码

        self.driver.find_element_by_id("com.hangtian.offcialvehicles:id/end_road_code_text").send_keys(end_road_code)#输入终止路码

        self.move_screen("0.40","0.78","0.40","0.65")

        self.driver.find_element_by_id("com.hangtian.offcialvehicles:id/getGPS_button").click()#点击获取GPS里程

        self.driver.find_element_by_id("com.hangtian.offcialvehicles:id/ok_text").click()#点击归队

        self.driver.find_element_by_accessibility_id("转到上一层级").click()#回到主页面


    def confirmation_fee(self):#确认费用

        self.driver.find_element_by_id("com.hangtian.offcialvehicles:id/radiobutton_usecar").click()#点击底部用车按钮

        self.driver.find_element_by_id("com.hangtian.offcialvehicles:id/my_apply_money_layout").click()#点击我的费用

        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.RelativeLayout[1]").click()
        #点击第一条用车费用单

        self.driver.find_element_by_id("com.hangtian.offcialvehicles:id/querenjine").click()#点击确认用车费用

        self.driver.find_element_by_accessibility_id("转到上一层级").click()  # 回到主页面




a=Gongwuyongche()
# a.login("name")
# a.apply_car_layout()
# a.my_apply_car_layout()
# a.unlogin()
a.login("name")
a.car_check_layout()
a.unlogin()
a.login("name")
a.scheduling_layout()
a.sent_layout()
a.rentrun_layout()
a.unlogin()
a.login('name')
a.confirmation_fee()