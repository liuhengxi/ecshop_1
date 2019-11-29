from common.send_method import SendMethod
from common.get_result import GetKeyword
class Goods:
    def __init__(self,url):
        self.url=url
    def goods(self,data):
        return SendMethod.send_method(self.url, data)
    def get_shoots_succeeds(self,data):
        res=self.goods(data)
        return GetKeyword.get_keyword(res,"succeed")
if __name__ == '__main__':
    url="http://ecshop.itsoso.cn/ECMobile/?url=/goods"
    data={"goods_id":89,"session":{"uid":"4364","sid":"f19e97f38edeb88794b292ca168a6953ba000e43"}}
    godd=Goods(url)
    print(godd.goods(data))