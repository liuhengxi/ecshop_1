"""
test_login.py文件
    1.封装页面业务:对页面上面多个元素操作后所实现的功能
    2.测试用例
"""

from interface.login_interface import Login
from interface.collection_get_interface import Colection
from interface.address_get_interface import Address
import ddt,unittest
import time
from common.mysql_mydb import Database


from common.operartion_Excel import Operationxcel
#准备测试数据
oper = Operationxcel('./datas/getCollection_data.xls')
get_data = oper.get_data_info()

@ddt.ddt
class TextLogin(unittest.TestCase):
    def setUp(self) -> None:
        self.url="http://ecshop.itsoso.cn/ECMobile/?url=/user/signin"
        self.get_address_url = "http://ecshop.itsoso.cn/ECMobile/?url=/address/list"

    def tearDown(self) -> None:
        # 关闭浏览器
        time.sleep(1)

    @ddt.data(*get_data)
    def test_login(self,data):
        self.login = Login(self.url)
        self.login_data = {"name": str(data["name"]), "password": str(data["password"])}
        # print(self.login_data)
        # print(self.login.login({"name": str(data["name"]), "password": str(data["password"])}))
        self.session = self.login.get_session(self.login_data)  # 获取登录后session

        self.address_data = {"session": self.session}  # 查看收货地址请求参数

        print(Address.get_address(self.get_address_url, self.address_data))#打印地址信息

        self.info=Address.get_address(self.get_address_url, self.address_data)
        #断言是否成功
        self.assertEqual(1, self.login.get_status_new(self.info)['succeed'], msg="断言失败")
        # self.assertEqual(1, self.login.get_status_(self.login_data)['succeed'], msg="断言失败")

        # print("*"*60)
        # sql = "select * from ecs_users where user_id=9608 "
        #
        # db=Database()
        # result=db.read_all(sql)
        # print(result)


if __name__ == '__main__':
    unittest.main()
