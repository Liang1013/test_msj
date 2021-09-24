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
class PageToolYl(Base):

    '''进入工具定位'''
    title = ("css selector", ".header_page>div:nth-child(2)>div:nth-child(2)>span")
    menu_title = (
        "css selector", ".header_page>div:nth-child(2)>div:nth-child(9)>div:nth-child(1)>div>div:nth-child(7)>div>span")

    '''断言'''
    yl_text = ("css selector", ".ant-table-row>td:nth-child(1)")

    '''小黑盒新品引流定位'''
    xhh_id = ("css selector",".form_container>div:nth-child(2)>div>div:nth-child(2)>div:nth-child(1)>div>textarea")
    xhh_bth = ("css selector",".form_container>div:nth-child(2)>div>div:nth-child(2)>div:nth-child(2)>div>button:nth-child(1)")


    '''手淘其他店铺商品详情定位'''
    spxq_bth = ("css selector",".channel_type>span:nth-child(2)")
    spxq_id = ("css selector",".form_container>div:nth-child(2)>div>div:nth-child(3)>div:nth-child(1)>div>input")
    spxq_jp_id = ("css selector",".form_container>div:nth-child(2)>div>div:nth-child(3)>div:nth-child(2)>div>textarea")
    button = ("css selector",".form_container>div:nth-child(2)>div>div:nth-child(3)>div:nth-child(3)>div>button:nth-child(1)")

    def is_xhh(self,bady_id):
        self.js_move_to_element(self.title)
        self.js_click(self.menu_title)
        self.js_sendkeys(self.xhh_id,bady_id)
        self.js_click(self.xhh_bth)

    def is_spxq(self,bady_id,jp_id):
        self.js_click(self.spxq_bth)
        self.js_sendkeys(self.spxq_id,bady_id)
        self.js_sendkeys(self.spxq_jp_id,jp_id)
        self.js_click(self.button)

    def is_yl_text(self,text):
        text = self.js_text_element(self.yl_text,text)
        self.driver.refresh()
        return text


if __name__ == "__main__":
    driver = webdriver.Chrome("/usr/local/bin/chromedriver")
    log = PageLogin(driver)
    yl = PageToolYl(driver)
    log.is_login()
    yl.is_xhh("633428877391")
    t = yl.is_yl_text("633428877391")
    print("小黑盒结果：",t)

    yl.is_spxq("644809028569","651586603362")
    t2 = yl.is_yl_text("644809028569")
    print("手淘商品详情结果：", t2)


    time.sleep(4)
    driver.quit()
