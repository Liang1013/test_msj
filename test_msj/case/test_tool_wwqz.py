from page.page_login import PageLogin
from page.page_tool_wwqz import PageToolWwqz
from selenium import webdriver
from common.route import Route
from common.logger import Log

import unittest,ddt

execlname = [
    {"bady_id":"644809028569","number":"淘_旺商务","b_number":"淘_旺商务1\n淘_旺商务2"}
]

@ddt.ddt
class TestToolWwqz(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.logger = Log("TestToolWwqz").get_log()
        cls.rou = Route().js_route_chrome()
        cls.driver = webdriver.Chrome(cls.rou)
        cls.log = PageLogin(cls.driver)
        cls.qz = PageToolWwqz(cls.driver)
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
    def test_wwqz_A(self,data):
        self.qz.is_single_wwqz(data["bady_id"],data["number"])
        text = self.qz.is_wwqz_text(data["bady_id"])
        print("单个权重评估返回结果：", text)
        if True == text:
            self.assertTrue(text)
            self.logger.info("单个权重评估搜索成功")
        else:
            self.logger.info("单个权重评估搜索失败")

    @ddt.data(*execlname)
    def test_wwqz_B(self, data):
        self.qz.is_batch_wwqz(data["b_number"])
        text = self.qz.is_wwqz_text(data["bady_id"])
        print("批量权重评估返回结果：", text)
        if True == text:
            self.assertTrue(text)
            self.logger.info("批量权重评估搜索成功")
        else:
            self.logger.info("批量权重评估搜索失败")

if __name__ == "__main__":
    unittest.main()