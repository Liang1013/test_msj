from page.page_login import PageLogin
from page.page_tool_yl import PageToolYl
from selenium import webdriver
from common.route import Route
from common.logger import Log

import unittest,ddt

execlname = [
    {"bady_id":"https://item.taobao.com/item.htm?spm=a230r.1.14.1.473117c5Eulvgd&id=644809028569&ns=1&abbucket=5#detail",
     "assert":"644809028569",
     "spxq_id":"644809028569","jp_id":"651586603362"}
]

@ddt.ddt
class TestToolYl(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.logger = Log("TestToolYl").get_log()
        cls.rou = Route().js_route_chrome()
        cls.driver = webdriver.Chrome(cls.rou)
        cls.log = PageLogin(cls.driver)
        cls.yl = PageToolYl(cls.driver)
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
    def test_yl_A(self,data):
        self.yl.is_xhh(data["bady_id"])
        xhh_text = self.yl.is_yl_text(data["assert"])
        print("小黑盒返回结果：",xhh_text)
        if True == xhh_text:
            self.assertTrue(xhh_text)
            self.logger.info("小黑盒搜索成功")
        else:
            self.logger.info("小黑盒搜索失败")

    @ddt.data(*execlname)
    def test_yl_B(self,data):
        self.yl.is_spxq(data["spxq_id"], data["jp_id"])
        spxq_text = self.yl.is_yl_text(data["spxq_id"])
        print("手淘商品详情返回结果：", spxq_text)
        if True == spxq_text:
            self.assertTrue(spxq_text)
            self.logger.info("手淘商品详情搜索成功")
        else:
            self.logger.info("手淘商品详情搜索失败")


if __name__ == "__main__":
    unittest.main()

