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

class PageToolZyj(Base):

    '''进入工具定位'''
    title = ("css selector",".header_page>div:nth-child(2)>div:nth-child(2)>span")
    menu_title = (
        "css selector",".header_page>div:nth-child(2)>div:nth-child(9)>div:nth-child(1)>div>div:nth-child(1)>div>span")

    '''输入框/按钮定位'''
    name = ("css selector",".ant-input")
    bth = ("css selector",".ant-btn")

    '''断言定位'''
    name_text = (
        "css selector",".query_detail>div:nth-child(1)>div:nth-child(2)>div>div>table>tbody>tr:nth-child(1)>td:nth-child(4)")

    def is_wangwang(self,text):
        self.js_move_to_element(self.title)
        self.js_click(self.menu_title)
        self.js_sendkeys(self.name,text)
        self.js_click(self.bth)

    def is_wangwang_text(self,text):
        return self.js_text_element(self.name_text,text)


if __name__ == "__main__":
    driver = webdriver.Chrome("/usr/local/bin/chromedriver")
    log = PageLogin(driver)
    wang = PageToolZyj(driver)
    log.is_login()
    wang.is_wangwang("淘_旺商务")
    t = wang.is_wangwang_text("淘_旺商务")
    print(t)

    time.sleep(4)
    driver.quit()