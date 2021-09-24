from page.page_login import PageLogin
from page.page_tool_ssewm import PageToolSsewm
from selenium import webdriver
from common.route import Route
from common.logger import Log

import unittest,ddt

execlname = [
    {"name":"针织开衫女",
     "id":"https://item.taobao.com/item.htm?spm=a211oj.20087502.6500797680.ditem5.7ac82a7b5Atu7J&id=652791704467&utparam=null",
     "assert":"652791704467"}
]

@ddt.ddt
class TestToolSsewm(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.logger = Log("TestToolSsewm").get_log()
        cls.rou = Route().js_route_chrome()
        cls.driver = webdriver.Chrome(cls.rou)
        cls.log = PageLogin(cls.driver)
        cls.sec = PageToolSsewm(cls.driver)
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
    def test_search_A(self,data):
        self.sec.is_search(
            data["name"],data["id"])
        text = self.sec.is_search_text(
            data["assert"])
        print("text返回结果：",text)
        if True == text:
            self.assertTrue(text)
            self.logger.info("搜索二维码成功")
        else:
            self.logger.info("搜索二维码失败")

if __name__ == "__main__":
    unittest.main()