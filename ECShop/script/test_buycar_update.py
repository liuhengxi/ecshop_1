import unittest
from common.get_result import GetKeyword
from interface.login_interface import Login
from interface.buycar_interface import Buycar
from common.mysql_db import DB
class Test_buycar_update(unittest.TestCase):
    def setUp(self) -> None:
        self.url_buycar_create = "http://ecshop.itsoso.cn/ECMobile/?url=/cart/create"
        self.url_login = "http://ecshop.itsoso.cn/ECMobile/?url=/user/signin"
        self.data_login = {"name": "test", "password": "123123"}
        self.url_buycar_list = "http://ecshop.itsoso.cn/ECMobile/?url=/cart/list"
        self.url_buycar_update="http://ecshop.itsoso.cn/ECMobile/?url=/cart/update"
        self.db=DB()
    def test_buycar_update(self):
        login = Login(self.url_login)
        uid = GetKeyword.get_keyword(login.login(self.data_login), "uid")
        sid = GetKeyword.get_keyword(login.login(self.data_login), "sid")
        data_buycar_list = {"session": {"uid": uid, "sid": sid}}
        data_buycar = {"spec": [], "session": {"uid": uid, "sid": sid}, "goods_id": 89, "number": 1}
        buycar = Buycar(self.url_buycar_create)
        buycar.buycar(data_buycar)
        # 数据库查询修改前
        key = "user_id"
        value = f"{uid}"
        table_data = "ecs_cart"
        data1 = self.db.read_all(key, value, table_data)
        buycar=Buycar(self.url_buycar_list)
        rec_id=buycar.get_buycar_rec_id(data_buycar_list)
        data_buycar_update={"new_number":3,"session":{"uid":uid,"sid":sid},"rec_id":rec_id}
        buycar_update=Buycar(self.url_buycar_update)
        res =buycar_update.get_buycar_succeed(data_buycar_update)
        # 数据库修改后
        data2 = self.db.read_all(key, value, table_data)
        self.assertEqual(res,1,msg="凉")
        self.assertEqual(data1,data2,msg='进行修改le呦')
if __name__ == '__main__':
    unittest.main()