# 注册
from common.send_method import SendMethod
from common.get_result import GetKeyword
class Register:
    def __init__(self,url):
        self.url=url
    def register(self,data):
        """注册"""
        return SendMethod.send_method(self.url,data)
    def get_succeed(self,data):
        """获取返回后的succeed"""
        re =self.register(data)
        return GetKeyword.get_keyword(re,"succeed")
if __name__ == '__main__':
    url="http://ecshop.itsoso.cn/ECMobile/?url=/user/signup "
    data={"field":[{"value":"551411"}],"email":"m16s1@123.com","name":"w4雨","password":"123456"}
    re=Register(url)
    # print(re.register(data))
    print(re.get_succeed(data))