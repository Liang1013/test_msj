from page.page_login import PageLogin
from page.page_tool_lsjcx import PageToolLsjcx
from common.route import Route
from common.logger import Log
from selenium import webdriver

import unittest,ddt

execlname = [
    {"body_id":"653162729716","assert":"豆豆早安"},
    {"body_id":
         "https://detail.tmall.com/item.htm?id=625344243181&ali_refid=a3_430582_1006:1151585377:N:hZcG4dHtUcwnfkICIG6QHOb42e0xC8an:d149d3ea47da8fb872a6d7bd4944fb6c&ali_trackid=1_d149d3ea47da8fb872a6d7bd4944fb6c&spm=a230r.1.14.11",
     "assert":"花娴旗舰店"}
]

@ddt.ddt
class TestToolLsjcx(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.logger = Log("TestToolLsjcx").get_log()
        cls.rou = Route().js_route_chrome()
        cls.driver = webdriver.Chrome(cls.rou)
        cls.log = PageLogin(cls.driver)
        cls.lsj = PageToolLsjcx(cls.driver)
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
    def test_lsj_A(self,data):
        self.lsj.is_tool_lsjcx(data["body_id"])
        text = self.lsj.is_tool_lsjcx_text(data["assert"])
        print("历史价查询结果：",text)
        if True == text:
            self.assertTrue(text)
            self.logger.info("历史价查询成功")
        else:
            self.logger.info("历史价查询失败")

if __name__ == "__main__":
    unittest.main()
