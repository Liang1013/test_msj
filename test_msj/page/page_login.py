from common.base import Base
from selenium import webdriver
from common.route import Route

import time

'''
ID = "id"
    XPATH = "xpath"
    LINK_TEXT = "link text"
    PARTIAL_LINK_TEXT = "partial link text"
    NAME = "name"
    TAG_NAME = "tag name"
    CLASS_NAME = "class name"
    CSS_SELECTOR = "css selector"
'''

class PageLogin(Base):

    '''登陆定位'''
    input = ("css selector",".content-container-form>form>div:nth-child(1)>div>div>span>input")
    paw = ("css selector",".content-container-form>form>div:nth-child(2)>div>div>span>input")
    bth = ("css selector",".content-container-form>span")

    '''登陆断言定位'''
    input_text = ("css selector",".ant-layout-header>div>div:nth-child(3)>div>span:nth-child(1)")
    input_text_fail = ("css selector", ".ant-message>span>div>div>div>span")


    def is_input(self,user):
        self.js_sendkeys(self.input,user)

    def is_paw(self,paw):
        self.js_sendkeys(self.paw,paw)

    def is_bth(self):
        self.js_click(self.bth)

    def is_login(self):
        self.parameter = Route().js_route_url("production") ##production生产环境地址，test测试环境地址
        self.driver.get(self.parameter["url"]) #打开登陆地址
        self.driver.maximize_window() #窗口最大化
        self.is_input(self.parameter["username"])
        self.is_paw(self.parameter["password"])
        self.is_bth()

    def is_login_text(self,suc,text):
        if suc=="1":
            return self.js_text_element(self.input_text,text)
        elif suc=="0":
            return self.js_text_element(self.input_text_fail,text)



if __name__ == "__main__":
    driver = webdriver.Chrome("/usr/local/bin/chromedriver")
    log = PageLogin(driver)
    log.is_login()
    t = log.is_login_text("0","密码错误")
    print(t)

    time.sleep(4)
    driver.quit()