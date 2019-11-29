from common.get_result import GetKeyword
from interface.login_interface import Login
from interface.goods_interface import Goods
import unittest
class Test_shoots(unittest.TestCase):
    def setUp(self) -> None:
        self.url_goot="http://ecshop.itsoso.cn/ECMobile/?url=/goods"
        self.url_login="http://ecshop.itsoso.cn/ECMobile/?url=/user/signin"
        self.data_login={"name":"test","password":"123123"}


    def test_goots(self):
        """商品查询流程"""
        login=Login(self.url_login)
        uid=GetKeyword.get_keyword(login.login(self.data_login),"uid")
        sid=GetKeyword.get_keyword(login.login(self.data_login),"sid")
        data_shoots={"goods_id":89,"session":{"uid":uid,"sid":sid}}
        goods=Goods(self.url_goot)
        res=goods.get_shoots_succeeds(data_shoots)
        self.assertEqual(res,1,msg='凉')

if __name__ == '__main__':
    unittest.TestCase()
    