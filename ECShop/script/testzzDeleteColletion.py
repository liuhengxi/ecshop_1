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
from interface.collection_delete_interface import Del_collection
import ddt,unittest
from common.mysql_mydb import Database
import time


from common.operartion_Excel import Operationxcel
#准备测试数据
oper = Operationxcel('./datas/getCollection_data.xls')
get_data = oper.get_data_info()


#  print(add_data)   [{'email': 'asd@163.com', 'address': '自贡彩灯'}, {'email': '123@qq.com', 'address': '自贡西山'}]

@ddt.ddt
class TextLogin(unittest.TestCase):
    def setUp(self) -> None:
        self.url="http://ecshop.itsoso.cn/ECMobile/?url=/user/signin"
        self.get_address_url = "http://ecshop.itsoso.cn/ECMobile/?url=/address/list"
        self.del_address_url="http://ecshop.itsoso.cn/ECMobile/?url=/address/delete"
        self.get_colection_url = "http://ecshop.itsoso.cn/ECMobile/?url=/user/collect/list"
        self.del_collection_url="http://ecshop.itsoso.cn/ECMobile/?url=/user/collect/delete"

    def tearDown(self) -> None:
        # 关闭浏览器
        time.sleep(1)

    @ddt.data(*get_data)
    def test_login(self, data):
        self.login = Login(self.url)
        self.login_data = {"name": str(data["name"]), "password": str(data["password"])}
        self.session = self.login.get_session(self.login_data)  # 获取登录后session
        self.address_data = {"session": self.session}  # 查看收货地址请求参数

        self.info = Colection.get_colection(self.get_colection_url, self.address_data)
        print(self.info)  # 打印收藏信息
        print("*"*50)

          # 收藏信息
        self.rec_id = self.login.get_rec_id(self.info)  # 获取rec_id
        print("收藏商品的rec_id:",self.rec_id)
        # print(type(self.rec_id))
        # 删除收藏
        self.address_data = {"session": self.session, "rec_id": self.rec_id[0]}
        #print(Del_collection.del_collection(self.del_collection_url, self.address_data))
        self.info=Del_collection.del_collection(self.del_collection_url, self.address_data)
        print(self.info)
        print("*"*60)



        sql = f"SELECT * FROM `ecs_collect_goods` where user_id=9608 and rec_id={self.rec_id[0]} "
        db = Database()
        result = db.read_one(sql)
        # print(result)
        # print(type(result))
        self.assertIsNone(result, msg="断言失败")


if __name__ == '__main__':
    unittest.main()
