import unittest
from common.get_result import GetKeyword
from interface.login_interface import Login
from interface.buycar_interface import Buycar
from common.mysql_db import DB
class Test_buycar_list(unittest.TestCase):
    def setUp(self) -> None:
        self.url_login = "http://ecshop.itsoso.cn/ECMobile/?url=/user/signin"
        self.data_login = {"name": "test", "password": "123123"}
        self.url_buycar="http://ecshop.itsoso.cn/ECMobile/?url=/cart/list "
        self.db=DB()
    def test_buy_car_list(self):
        login = Login(self.url_login)
        uid = GetKeyword.get_keyword(login.login(self.data_login), "uid")
        sid = GetKeyword.get_keyword(login.login(self.data_login), "sid")
        data_buycar={"session":{"uid":uid,"sid":sid}}
        buycar=Buycar(self.url_buycar)
        res=buycar.get_buycar_succeed(data_buycar)
        # 查看数据库是否有
        key = "user_id"
        value = f"{uid}"
        table_data = "ecs_cart"
        datas=self.db.read_one(key,value,table_data)
        self.assertEqual(res,1,msg="凉")
        self.assertIsNone(datas,msg="数据库商品不为空")
if __name__ == '__main__':
    unittest.main()