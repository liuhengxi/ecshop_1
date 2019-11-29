import unittest
from interface.register_interface import Register
from common.operartion_Excel import Operationxcel
from interface.login_interface import Login
import ddt
from common.mysql_db import DB
oper = Operationxcel("./datas/test_register.xlsx")
test_data = oper.get_data_info()
@ddt.ddt
class Test_register(unittest.TestCase):
    def setUp(self) -> None:
        self.url="http://ecshop.itsoso.cn/ECMobile/?url=/user/signup"
        self.db=DB()
        self.log=Login('http://ecshop.itsoso.cn/ECMobile/?url=/user/signin')
    @ddt.data(*test_data)
    def test_register01(self,data):
        register=Register(self.url)
        res_data={"field":str([{"value":data['value']}]),
                  "email":str(data['email']),
                  "name":str(data['name']),
                  "password":str(data['password'])}
        result=register.get_succeed(res_data)
        # 查看数据库是否注册成功

        self.uid=self.log.get_login_uid({"name":str(data['name']),"password":str(data['password'])} )
        key="user_id"
        value=f"{self.uid}"
        table_data="ecs_users"
        datas=self.db.read_one(key,value,table_data)
        # # # 将测试数据删除
        table_name="ecs_users"
        table="user_id"
        value=f"{self.uid}"
        self.db.delete_all(table_name,table,value)
        self.assertEqual(result, data['succeed'], msg='凉了')
        self.assertIsNone(datas,msg="账号不为空")
if __name__ == '__main__':
    unittest.main()