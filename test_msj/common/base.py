from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from common.logger import Log

'''
Example:
            from selenium.webdriver.support.ui import WebDriverWait \n
            element = WebDriverWait(driver, 10).until(lambda x: x.find_element_by_id("someId")) \n
            is_disappeared = WebDriverWait(driver, 30, 1, (ElementNotVisibleException)).\ \n
                        until_not(lambda x: x.find_element_by_id("someId").is_displayed())
'''
class Base():

    def __init__(self,driver:webdriver.Chrome):
        self.logger = Log("Base").get_log()
        self.driver = driver
        self.times = 10


    def js_find_element(self,locale):
        '''
        封装WebDriverWait查找事件方法
        :param locale:传入定位事件
        :return:默认0.5s查找一次定位，共20s，超出20s抛出异常
        '''
        try:
            element = WebDriverWait(self.driver,self.times)\
                .until(lambda x: x.find_element(*locale))
            return element
        except:
            self.logger.error("%s 页面未能找到此%s 元素"%(locale))


    def js_text_element(self,locale,text):
        '''
        封装判断定位方法
        :param locale:传入定位事件
        :param text:传入判断预期结果
        :return:默认0.5s查找一次定位，共20s，超出20s抛出异常
        '''
        try:
            element = WebDriverWait(self.driver,self.times)\
                .until(EC.text_to_be_present_in_element(locale,text))
            return element
        except:
            self.logger.error("%s 页面未能找到此%s 元素"%(locale))
            return False


    def js_sendkeys(self,locale,text):
        '''
        通过WebDriverWait，封装sendkeys方法
        :param locale:输入框事件
        :param text:输入的值
        :return:
        '''
        self.js_find_element(locale)\
            .send_keys(text)

    def js_click(self,locale):
        '''
        通过WebDriverWait，封装click方法
        :param locale:点击事件
        :return:
        '''
        self.js_find_element(locale)\
            .click()

    def js_clear(self,locale):
        '''
        通过WebDriverWait，封装clear方法
        :param locale: 清空输入框数据
        :return:
        '''
        self.js_find_element(locale)\
            .clear()

    def js_move_to_element(self,locale):
        '''
        封装鼠标悬浮方法
        :param locale:
        :return:
        '''
        ActionChains(self.driver).move_to_element(
            self.js_find_element(locale)).perform()

    def js_double_clear(self,locale):
        '''
        封装输入框双击事件
        :param locale: 使用与clear方法失效，使用此方法实现情况作用
        :return:
        '''
        ActionChains(self.driver).double_click(
            self.js_find_element(locale)).perform()


