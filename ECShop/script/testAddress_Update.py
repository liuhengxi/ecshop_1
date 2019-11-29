"""
test_login.py文件
    1.封装页面业务:对页面上面多个元素操作后所实现的功能
    2.测试用例
"""

from interface.login_interface import Login
from interface.collection_get_interface import Colection
from interface.address_get_interface import Address
from interface.address_add_interface import Add_collection
from interface.address_delete_interface import Del_address
from interface.address_update_interface import Update_address
import ddt,unittest
from common.mysql_mydb import Database
import time


from common.operartion_Excel import Operationxcel
#准备测试数据
oper = Operationxcel('./datas/updateAddress_data.xls')
update_data = oper.get_data_info()


#  print(add_data)   [{'email': 'asd@163.com', 'address': '自贡彩灯'}, {'email': '123@qq.com', 'address': '自贡西山'}]

@ddt.ddt
class TextLogin(unittest.TestCase):
    def setUp(self) -> None:
        self.url="http://ecshop.itsoso.cn/ECMobile/?url=/user/signin"
        self.get_address_url = "http://ecshop.itsoso.cn/ECMobile/?url=/address/list"
        self.del_address_url="http://ecshop.itsoso.cn/ECMobile/?url=/address/delete"
        self.update_address_url = "http://ecshop.itsoso.cn/ECMobile/?url=/address/update"

    def tearDown(self) -> None:
        # 关闭浏览器
        time.sleep(1)

    @ddt.data(*update_data)
    def test_login(self, data):
        self.login = Login(self.url)
        self.login_data = {"name": "xxy", "password": "123456"}
        self.session = self.login.get_session(self.login_data)  # 获取登录后session
        self.address_data = {"session": self.session}  # 查看收货地址请求参数
        self.info = Address.get_address(self.get_address_url, self.address_data)  # 地址所有信息
        print(self.info)  # 打印地址信息
        print("*"*70)


        self.address_id = self.login.get_addrid(self.info)  # 获取地址id
        print("地址ID:",self.address_id)#获取所有 地址id
        #print(type(self.address_id))   #<class 'str'>

        # 更新地址
        self.address_data = {"address": {"default_address": 0, "consignee": "user",
                                        "tel": "1898976579464", "zipcode": "621000",
                                        "country": "4044", "city": "0", "id": 0,
                                        "email": "98784564@qq.com", "address": data['address'],
                                        "province": "0", "district": "0", "mobile": ""}, "address_id": str(self.address_id),
                            "session": self.session}
        #print(Update_address.update_address(self.update_address_url, self.address_data))

        self.info=Update_address.update_address(self.update_address_url, self.address_data)
        print(self.info)
        print(type(self.info))

        # self.assertEqual(1, self.login.get_status_new(self.info)['succeed'], msg="断言失败")
        print("*"*60)
        #
        # 查看数据库 是否已删除地址
        sql = f"SELECT * FROM `ecs_user_address` where user_id=9608 and address={self.address_id}"
        db = Database()
        result = db.read_all(sql)
        # print(result)
        # print(type(result))
        self.assertIsNotNone(result, msg="断言失败")



if __name__ == '__main__':
    unittest.main()
