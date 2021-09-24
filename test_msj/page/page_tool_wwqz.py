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
class PageToolWwqz(Base):

    '''进入工具定位'''
    title = ("css selector", ".header_page>div:nth-child(2)>div:nth-child(2)>span")
    menu_title = (
        "css selector", ".header_page>div:nth-child(2)>div:nth-child(9)>div:nth-child(1)>div>div:nth-child(8)>div>span")

    '''单个权重评估定位'''
    s_bady_id = ("css selector",".form_box>div:nth-child(2)>div:nth-child(2)>input")
    s_number = ("css selector",".form_box>div:nth-child(3)>div:nth-child(2)>input")


    '''批量权重评估定位'''
    b_bth = ("css selector",".form_box>div:nth-child(1)>div:nth-child(2)>div:nth-child(2)")
    b_number = ("css selector",".form_box>div:nth-child(4)>div:nth-child(2)>textarea")

    '''搜索按钮'''
    bth = ("css selector", ".form_box>button")

    '''断言'''
    wwqz_text = ("css selector",".ant-table-tbody>tr>td:nth-child(3)")


    def is_single_wwqz(self,bady_id,number):
        self.js_move_to_element(self.title)
        self.js_click(self.menu_title)
        self.js_sendkeys(self.s_bady_id,bady_id)
        self.js_sendkeys(self.s_number,number)
        self.js_click(self.bth)

    def is_batch_wwqz(self,text):
        self.js_click(self.b_bth)
        self.js_clear(self.b_number)
        self.js_sendkeys(self.b_number,text)
        self.js_click(self.bth)


    def is_wwqz_text(self,text):
        return self.js_text_element(self.wwqz_text,text)

if __name__ == "__main__":
    driver = webdriver.Chrome("/usr/local/bin/chromedriver")
    log = PageLogin(driver)
    qz = PageToolWwqz(driver)
    log.is_login()
    qz.is_single_wwqz("644809028569","淘_旺商务")

    t = qz.is_wwqz_text("644809028569")
    print("t",t)

    qz.is_batch_wwqz("淘_旺商务1\n淘_旺商务2")

    t2 = qz.is_wwqz_text("644809028569")
    print("t2",t2)

    time.sleep(4)
    driver.quit()