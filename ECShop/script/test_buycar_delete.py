import unittest
from common.get_result import GetKeyword
from interface.login_interface import Login
from interface.buycar_interface import Buycar
class Test_buycar_delete(unittest.TestCase):
    def setUp(self) -> None:
        self.url_login = "http://ecshop.itsoso.cn/ECMobile/?url=/user/signin"
        self.data_login = {"name": "test", "password": "123123"}
        self.url_buycar_create = "http://ecshop.itsoso.cn/ECMobile/?url=/cart/create"
        self.url_buycar_list = "http://ecshop.itsoso.cn/ECMobile/?url=/cart/list"
        self.url_buycar_delete="http://ecshop.itsoso.cn/ECMobile/?url=/cart/delete"
    def test_buycar_delete(self):
        login = Login(self.url_login)
        uid = GetKeyword.get_keyword(login.login(self.data_login), "uid")
        sid = GetKeyword.get_keyword(login.login(self.data_login), "sid")
        data_create={"spec":[],"session":{"uid":uid,"sid":sid},"goods_id":89,"number":1}
        buycar_create=Buycar(self.url_buycar_create)
        buycar_create.buycar(data_create)
        data_list={"session":{"uid":uid,"sid":sid}}
        buycar_list=Buycar(self.url_buycar_list)
        rec_id=buycar_list.get_buycar_rec_id(data_list)
        data_delete={"session":{"uid":uid,"sid":sid},"rec_id":rec_id}
        buycar_delete=Buycar(self.url_buycar_delete)
        res=buycar_delete.get_buycar_succeed(data_delete)
        self.assertEqual(res,1,msg="凉")
if __name__ == '__main__':
    unittest.main()