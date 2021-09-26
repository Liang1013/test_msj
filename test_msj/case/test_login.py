from selenium import webdriver
from page.page_login import PageLogin
from common.route import Route
from common.logger import Log

import unittest,ddt

ecl = Route().js_route_execl("login.xlsx")

@ddt.ddt
class TestLogin(unittest.TestCase):

    @classmethod
    def setUp(self) -> None:
        self.logger = Log("TestLogin").get_log()
        self.rou = Route().js_route_chrome()
        self.testurl = Route().js_route_url("production") #production生产环境地址，test测试环境地址
        self.driver = webdriver.Chrome(self.rou)
        self.log = PageLogin(self.driver)
        self.driver.maximize_window()
        self.driver.get(self.testurl["url"])
        self.logger.info("----------开始执行测试用例----------")

    @classmethod
    def tearDown(self) -> None:
        self.logger.info("--------------pass---------------")
        self.driver.quit()

    def login(self,user,paw):
        self.log.is_input(user)
        self.log.is_paw(paw)
        self.log.is_bth()

    @ddt.data(*ecl)
    def test_login_A(self,data):
        '''msj登陆成功测试用例'''
        self.login(
            data["user"],data["paw"])
        text = self.log.is_login_text(
            data["suc"],data["assert"])
        print("text返回结果：",text)
        if True == text:
            self.assertTrue(text)
            self.logger.info("msj登陆成功")
        else:
            self.logger.info("msj登陆失败")

if __name__ == "__main__":
    unittest.main()