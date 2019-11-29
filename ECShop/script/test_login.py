from interface.login_interface import Login
import unittest
from common.operartion_Excel import Operationxcel
import ddt

oper = Operationxcel('./datas/login_data.xls')
test_data = oper.get_data_info()



@ddt.ddt
class Test_login(unittest.TestCase):
    def setUp(self) -> None:
        self.url = "http://ecshop.itsoso.cn/ECMobile/?url=/user/signin"

    @ddt.data(*test_data)
    def test_login01(self, data):
        login = Login(self.url)
        # 去登陆
        # self.login.login({'name': str(data['name']),
        #                   "password": str(data['password'])})
        res_data={'name': str(data['name']),"password": str(data['password'])}
        result=login.get_succeed(res_data)
        self.assertEqual(result,data['succeed'],msg='凉了')
if __name__ == '__main__':
    unittest.main()
