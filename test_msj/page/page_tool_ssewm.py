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
class PageToolSsewm(Base):

    '''进入工具定位'''
    title = ("css selector", ".header_page>div:nth-child(2)>div:nth-child(2)>span")
    menu_title = (
        "css selector", ".header_page>div:nth-child(2)>div:nth-child(9)>div:nth-child(1)>div>div:nth-child(3)>div>span")

    '''输入框定位'''
    name = ("css selector",".form_box>div:nth-child(1)>div>input")
    body_id = ("css selector",".form_box>div:nth-child(2)>div>input")
    bth = ("css selector",".form_box>div:nth-child(3)>div>button:nth-child(1)")

    '''断言定位'''
    search_text = ("css selector",".ant-table-tbody>tr>td:nth-child(3)")

    def is_search(self,name,id):
        self.js_move_to_element(self.title)
        self.js_click(self.menu_title)
        self.js_sendkeys(self.name,name)
        self.js_sendkeys(self.body_id,id)
        self.js_click(self.bth)

    def is_search_text(self,text):
        return self.js_text_element(self.search_text,text)

if __name__ == "__main__":
    driver = webdriver.Chrome("/usr/local/bin/chromedriver")
    log = PageLogin(driver)
    sec = PageToolSsewm(driver)
    log.is_login()
    sec.is_search("针织外套","652188561191")
    t = sec.is_search_text("652188561191")
    print(t)

    time.sleep(4)
    driver.quit()