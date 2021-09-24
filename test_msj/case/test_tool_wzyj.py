from page.page_tool_wzyj import PageToolZyj
from page.page_login import PageLogin
from selenium import webdriver
from common.route import Route
from common.logger import Log

import unittest,ddt

execlname = [
    {"name":"麦苗科技001","assert":"麦苗科技001"}
]

@ddt.ddt
class TestToolWzyj(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.logger = Log("TestToolWzyj").get_log()
        cls.rou = Route().js_route_chrome()
        cls.driver = webdriver.Chrome(cls.rou)
        cls.log = PageLogin(cls.driver)
        cls.wang = PageToolZyj(cls.driver)
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
    def test_wang_A(self,data):
        '''
        旺旺照妖镜测试用例
        :param data:
        :return:
        '''
        self.wang.is_wangwang(
            data["name"])
        text = self.wang.is_wangwang_text(
            data["assert"])
        print("text返回结果：",text)
        if True == text:
            self.assertTrue(text)
            self.logger.info("旺旺照妖镜查询成功")
        else:
            self.logger.info("旺旺照妖镜查询失败")

if __name__ == "__main__":
    unittest.main()