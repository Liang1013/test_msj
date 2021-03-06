from common.excelutil import ExcelUtil

import os,yaml

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
        propath = os.path.dirname(os.path.dirname
                                  (os.path.realpath(__file__)))
        filepath = os.path.join(
            propath,route)
        return filepath

    def js_route_url(self,url_name):
        '''
        获取url：yaml文件路径
        :param url_name:
        :return:
        '''
        propath = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
        filepath = os.path.join(propath, "data", "login_url.yaml")
        with open(filepath, 'r', encoding='utf-8') as f:
            parameter = yaml.load(f,Loader=yaml.FullLoader)
        return parameter[url_name]

    def js_route_mail(self,mail):
        '''
        获取邮箱yaml文件路径
        :param url_name:
        :return:
        '''
        propath = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
        filepath = os.path.join(propath, "data", "sendmail.yaml")
        with open(filepath, 'r', encoding='utf-8') as f:
            parameter = yaml.load(f,Loader=yaml.FullLoader)
        return parameter[mail]

if __name__== "__main__":
    path = Route().js_route_mail("mail")
    #t = path.js_route_url("test")
    print(path)