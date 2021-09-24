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

class PageToolTkl(Base):


    '''进入工具定位'''
    title = ("css selector", ".header_page>div:nth-child(2)>div:nth-child(2)>span")
    menu_title = (
        "css selector", ".header_page>div:nth-child(2)>div:nth-child(9)>div:nth-child(1)>div>div:nth-child(5)>div>span")

    input = ("css selector",".tao-form>div:nth-child(1)>input")
    btn = ("css selector",".tao-form>div:nth-child(2)>button")

    tkl_text = ("css selector",".ant-message>span>div>div>div>span")


    def is_tkl(self,bady_id):
        self.js_move_to_element(self.title)
        self.js_click(self.menu_title)
        self.js_sendkeys(self.input,bady_id)
        self.js_click(self.btn)

    def is_tkl_text(self,text):
        return self.js_text_element(
            self.tkl_text,text)

if __name__ == "__main__":

    driver = webdriver.Chrome("/usr/local/bin/chromedriver")
    log = PageLogin(driver)
    tkl = PageToolTkl(driver)
    log.is_login()
    tkl.is_tkl("652988309188")

    t = tkl.is_tkl_text("该链接生成失败,请稍后重试")
    print(t)

    time.sleep(4)
    driver.quit()