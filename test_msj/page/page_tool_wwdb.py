from common.base import Base
from selenium import webdriver
from page.page_login import PageLogin

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

class PageToolWwdb(Base):

    '''进入工具定位'''
    title = ("css selector",".header_page>div:nth-child(2)>div:nth-child(2)>span")
    menu_title = (
    "css selector",".header_page>div:nth-child(2)>div:nth-child(9)>div:nth-child(1)>div>div:nth-child(2)>div>span")

    '''输入框定位'''
    baby_id = ("css selector",".form_box>div:nth-child(1)>div>input")
    words = ("css selector",".form_box>div:nth-child(2)>div>input")
    marking = ("css selector",".form_box>div:nth-child(3)>div>textarea")
    bth = ("css selector",".ant-btn-primary")

    '''断言定位'''
    marking_text = ("css selector",".ant-message>span>div>div>div>span")


    def is_marking(self,id,name,number):
        self.js_move_to_element(self.title)
        self.js_click(self.menu_title)
        self.js_sendkeys(self.baby_id,id)
        self.js_sendkeys(self.words,name)
        self.js_sendkeys(self.marking,number)
        self.js_click(self.bth)

    def is_marking_text(self,text):
        return self.js_text_element(self.marking_text,text)

if __name__ == "__main__":
    driver = webdriver.Chrome("/usr/local/bin/chromedriver")
    log = PageLogin(driver)
    mk = PageToolWwdb(driver)
    log.is_login()
    mk.is_marking("612558620161","实木电视柜","淘_旺商务")
    t = mk.is_marking_text("打标异常")
    print(t)

    time.sleep(4)
    driver.quit()