from common.base import Base
from page.page_login import PageLogin
from selenium import webdriver

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

class PageToolDSR(Base):


    '''进入工具定位'''
    title = ("css selector", ".header_page>div:nth-child(2)>div:nth-child(3)>span")
    menu_title = (
        "css selector", ".header_nav>div:nth-child(9)>div:nth-child(2)>div>div:nth-child(4)>div>span")

    '''DSR查询定位'''
    wwh = ("css selector",".form_inp")
    bth = ("css selector",".ant-btn")

    dsr_text = ("css selector",".ant-descriptions-view>table>tbody>tr:nth-child(1)>td:nth-child(4)")


    def is_tool_dsr(self,iphone):
        self.js_move_to_element(self.title)
        self.js_click(self.menu_title)
        self.js_sendkeys(self.wwh,iphone)
        self.js_click(self.bth)

    def is_tool_dsr_text(self,text):
        return self.js_text_element(self.dsr_text,text)


if __name__== "__main__":
    driver = webdriver.Chrome("/usr/local/bin/chromedriver")
    log = PageLogin(driver)
    dsr = PageToolDSR(driver)

    log.is_login()
    dsr.is_tool_dsr("淘_旺商务")

    t = dsr.is_tool_dsr_text("简沐家具铺")
    print(t)

    time.sleep(4)
    driver.quit()
