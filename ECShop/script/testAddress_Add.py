"""
test_login.py文件
    1.封装页面业务:对页面上面多个元素操作后所实现的功能
    2.测试用例
"""

from interface.login_interface import Login
from interface.collection_get_interface import Colection
from interface.address_get_interface import Address
from interface.address_add_interface import Add_collection
import ddt,unittest
import time
from common.mysql_mydb import Database




from common.operartion_Excel import Operationxcel
#准备测试数据
oper = Operationxcel('../datas/addAddress_data.xls')
add_data = oper.get_data_info()

@ddt.ddt
class TextLogin(unittest.TestCase):
    def setUp(self) -> None:
        self.url="http://ecshop.itsoso.cn/ECMobile/?url=/user/signin"
        self.add_address_url = "http://ecshop.itsoso.cn/ECMobile/?url=/address/add"
        self.get_address_url = "http://ecshop.itsoso.cn/ECMobile/?url=/address/list"

    def tearDown(self) -> None:
        # 关闭浏览器
        time.sleep(1)

    @ddt.data(*add_data)
    def test_login(self,data):
        self.login = Login(self.url)
        self.login_data = {"name":"xxy","password":"123456"}
        # print(self.login_data)
        # print(self.login.login({"name": str(data["name"]), "password": str(data["password"])}))
        self.session = self.login.get_session(self.login_data)  # 获取登录后session

        self.address_data = {"address": {"default_address": 0, "consignee": "zzc",
                                    "tel": "18080263593", "zipcode": "621000",
                                    "country": "4044", "city": "",
                                    "id": 0, "email":data["email"],
                                    "address":data["address"], "province": "",
                                    "district": "", "mobile": ""}, "session": self.session}

        self.info=Add_collection.add_address(self.add_address_url, self.address_data)
        print(self.info)

        print("*" * 60)


        #查看地址 与数据库 地址id作比较
        self.address_data = {"session": self.session}  # 查看收货地址请求参数
        print(Address.get_address(self.get_address_url, self.address_data))  # 打印地址信息
        self.info = Address.get_address(self.get_address_url, self.address_data)
        # 断言是否成功
        result1=self.login.get_addrids(self.info)
        # print(type(result))
        result1=str(result1[0])
        print(result1)
        print("*" * 60)


        sql = "SELECT * FROM `ecs_user_address` where user_id=10334 order by address_id desc "
        db = Database()
        result = db.read_all(sql)
        print(result)

        result2=str(result[0]['address_id'])

        # #断言
        self.assertEqual(result1, result2, msg="断言失败")

if __name__ == '__main__':
    unittest.main()
