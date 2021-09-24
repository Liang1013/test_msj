from page.page_login import PageLogin
from page.page_tool_wwdb import PageToolWwdb
from selenium import webdriver
from common.route import Route
from common.logger import Log

import unittest,ddt

execlname = [
    {"id":"612558620161","words":"实木电视柜",
     "marking":"淘_旺商务","assert":"打标异常"}
]

@ddt.ddt
class TestToolWwdb(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.logger = Log("TestToolWwdb").get_log()
        cls.rou = Route().js_route_chrome()
        cls.driver = webdriver.Chrome(cls.rou)
        cls.log = PageLogin(cls.driver)
        cls.mk = PageToolWwdb(cls.driver)
        cls.log.is_login()

    @classmethod
    def setUp(self) -> None:
        self.logger.info("----------开始执行测试用例----------")

    @classmethod
    def tearDown(self) -> None:
        self.logger.info("--------------pass---------------")

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    @ddt.data(*execlname)
    def test_marking_A(self,data):
        self.mk.is_marking(
            data["id"],data["words"],data["marking"])
        text = self.mk.is_marking_text(
            data["assert"])
        print("text返回结果：",text)
        if True == text:
            self.assertTrue(text)
            self.logger.info("旺旺打标异常结果成功")
        else:
            self.logger.info("旺旺打标异常结果失败")

if __name__ == "__main__":
    unittest.main()