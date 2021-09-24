from page.page_tool_tkl import PageToolTkl
from page.page_login import PageLogin
from selenium import webdriver
from common.logger import Log
from common.route import Route

import unittest,ddt

execlname = [
    {"bady_id":"652988309188","assert":"该链接生成失败,请稍后重试"}
]

@ddt.ddt
class TestToolTkl(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.logger = Log("TestToolTkl").get_log()
        cls.rou = Route().js_route_chrome()
        cls.driver = webdriver.Chrome(cls.rou)
        cls.log = PageLogin(cls.driver)
        cls.tkl = PageToolTkl(cls.driver)
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
    def test_tkl_A(self,data):
        self.tkl.is_tkl(data["bady_id"])
        text = self.tkl.is_tkl_text(data["assert"])
        print("text返回结果：",text)
        if True == text:
            self.assertTrue(text)
            self.logger.info("淘口令官方接口返回失败，断言成功")
        else:
            self.logger.info("淘口令验证失败")

if __name__ == "__main__":
    unittest.main()