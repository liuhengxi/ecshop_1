import unittest
from common.get_result import GetKeyword
from interface.login_interface import Login
from interface.buycar_interface import Buycar
from common.mysql_db import DB
class Test_buycar_create(unittest.TestCase):
    def setUp(self) -> None:
        self.url_buycar="http://ecshop.itsoso.cn/ECMobile/?url=/cart/create"
        self.url_login = "http://ecshop.itsoso.cn/ECMobile/?url=/user/signin"
        self.data_login = {"name": "test", "password": "123123"}
        self.db=DB()
    def test_buycar_create(self):

        login = Login(self.url_login)
        uid = GetKeyword.get_keyword(login.login(self.data_login), "uid")
        sid = GetKeyword.get_keyword(login.login(self.data_login), "sid")
        # 清空
        table_name = 'ecs_cart'
        table = 'user_id'
        value = uid
        self.db.delete_all(table_name, table, value)
        data_buycar={"spec":[],"session":{"uid":uid,"sid":sid},"goods_id":89,"number":1}
        buycar=Buycar(self.url_buycar)
        res = buycar.get_buycar_succeed(data_buycar)

        # 查询数据库是否添加成功
        key = "user_id"
        value = f"{uid}"
        table_data = "ecs_cart"
        datas = self.db.read_all(key, value, table_data)
        # 删除
        self.db.delete_all(table_name, table, value)
        self.assertEqual(res, 1, msg="凉")
        self.assertIsNone(datas)
if __name__ == '__main__':
    unittest.main()
