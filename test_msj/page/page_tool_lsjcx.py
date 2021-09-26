from page.page_login import PageLogin
from common.base import Base
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

class PageToolLsjcx(Base):

    '''进入工具定位'''
    title = ("css selector", ".header_page>div:nth-child(2)>div:nth-child(3)>span")
    menu_title = (
        "css selector", ".header_nav>div:nth-child(9)>div:nth-child(2)>div>div:nth-child(5)>div>span")

    ''''''
    body_id = ("css selector",".form_inp")
    bth = ("css selector",".ant-btn")

    lsj_text = ("css selector",".ant-descriptions-view>table>tbody>tr:nth-child(3)>td")

    def is_tool_lsjcx(self,body_id):
        self.js_move_to_element(self.title)
        self.js_click(self.menu_title)
        self.js_double_clear(self.body_id)
        self.js_sendkeys(self.body_id,body_id)
        self.js_click(self.bth)


    def is_tool_lsjcx_text(self,text):
        return self.js_text_element(self.lsj_text,text)

if __name__ == "__main__":
    driver = webdriver.Chrome("/usr/local/bin/chromedriver")
    log = PageLogin(driver)
    lsj = PageToolLsjcx(driver)
    log.is_login()

    lsj.is_tool_lsjcx("653162729716")

    t = lsj.is_tool_lsjcx_text("豆豆早安")
    print(t)

    time.sleep(4)
    driver.quit()