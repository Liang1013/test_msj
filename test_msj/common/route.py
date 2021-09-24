from common.excelutil import ExcelUtil

import os

class Route():

    def js_route_chrome(self):
        '''
        获取chromedriver路径
        :return: 返回路径
        '''
        propath = os.path.dirname(
            os.path.dirname(os.path.realpath(__file__)))
        filepath = os.path.join(
            propath, "data", "chromedriver")
        return filepath

    def js_route_execl(self,text):
        '''
        获取xlxs路径，使用ExcelUtil方法解析表格数据
        :return: 返回获取表格的数据
        '''
        propath = os.path.dirname(
            os.path.dirname(os.path.realpath(__file__)))
        filepath = os.path.join(
            propath, "data",text)
        data = ExcelUtil(filepath)
        return data.dict_data()

    def js_route_report(self,route):
        '''
        获取report路径
        :param route:父类文件夹名称
        :return: 返回路径
        '''
        propath = os.path.dirname(
            os.path.dirname(os.path.realpath(__file__)))
        filepath = os.path.join(
            propath,route)
        return filepath

if __name__== "__main__":
    path = Route()
    t = path.js_route_chrome()
    print(t)