from common.send_method import SendMethod
from common.get_result import GetKeyword
class Buycar:
    def __init__(self,url):
        self.url=url
    def buycar(self,data):
        return SendMethod.send_method(self.url,data)
    def get_buycar_succeed(self,data):
        res=self.buycar(data)
        return GetKeyword.get_keyword(res,"succeed")
    def get_buycar_goods_id(self,data):
        res = self.buycar(data)
        return GetKeyword.get_keyword(res, "goods_id")
    def get_buycar_rec_id(self,data):
        res = self.buycar(data)
        return GetKeyword.get_keywords(res, "rec_id")
if __name__ == '__main__':
    url="http://ecshop.itsoso.cn/ECMobile/?url=/cart/create"
    data={"spec":[],"session":{"uid":"4364","sid":"f19e97f38edeb88794b292ca168a6953ba000e43"},"goods_id":89,"number":1}
