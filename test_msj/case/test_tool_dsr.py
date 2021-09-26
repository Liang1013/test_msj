from page.page_login import PageLogin
from page.page_tool_dsr import PageToolDSR
from common.route import Route
from common.logger import Log
from selenium import webdriver

import unittest,ddt

execlname = [
    {"iphone":"淘_旺商务","assert":"简沐家具铺"}
]

@ddt.ddt
class TestTollDSR(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.logger = Log("TestTollDSR").get_log()
        cls.rou = Route().js_route_chrome()
        cls.driver = webdriver.Chrome(cls.rou)
        cls.log = PageLogin(cls.driver)
        cls.dsr = PageToolDSR(cls.driver)
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
    def test_dsr_A(self,data):
        self.dsr.is_tool_dsr(data["iphone"])
        text = self.dsr.is_tool_dsr_text(data["assert"])
        print("DSR查询结果：",text)
        if True == text:
            self.assertTrue(text)
            self.logger.info("DSR查询成功")
        else:
            self.logger.info("DSR查询失败")

if __name__ == "__main__":
    unittest.main()