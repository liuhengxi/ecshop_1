"""
test_login.py文件
    1.封装页面业务:对页面上面多个元素操作后所实现的功能
    2.测试用例
"""

from interface.login_interface import Login
from interface.collection_add_interface import Add_collection
from interface.collection_get_interface import Colection
import ddt,unittest
from common.mysql_mydb import Database
import time


from common.operartion_Excel import Operationxcel
#准备测试数据
oper = Operationxcel('./datas/addCollection_data.xls')
add_data = oper.get_data_info()

@ddt.ddt
class TextLogin(unittest.TestCase):
    def setUp(self) -> None:
        self.url="http://ecshop.itsoso.cn/ECMobile/?url=/user/signin"
        self.add_collection_url = "http://ecshop.itsoso.cn/ECMobile/?url=/user/collect/create"
        self.get_colection_url = "http://ecshop.itsoso.cn/ECMobile/?url=/user/collect/list"
    def tearDown(self) -> None:
        # 关闭浏览器
        time.sleep(1)

    @ddt.data(*add_data)
    def test_login(self,data):
        self.login = Login(self.url)
        self.login_data = {"name":"xxy","password":"123456"}

        #添加收藏
        print("*" * 70)
        self.session = self.login.get_session(self.login_data)
        self.address_data = {"session": self.session, "goods_id": str(data["goods_id"])}

        self.info = Add_collection.add_collection(self.add_collection_url, self.address_data)
        print(self.info)
        print("*" * 70)

        #查看收藏
        self.address_data = {"session": self.session}  # 查看收货地址请求参数

        self.info = Colection.get_colection(self.get_colection_url, self.address_data)
        print(self.info)  # 打印收藏信息

        rec_id=self.login.get_rec_id(self.info) #得到rec_id
        result1=str(rec_id[0])
        print(rec_id)
        print("*" * 70)


        #查看数据库

        sql = "SELECT * FROM `ecs_collect_goods` where user_id=9608  "
        db = Database()
        result = db.read_all(sql)
        print(result)
        result2 = str(result[0]['rec_id'])
        print("*"*70)
        self.assertEqual(result1, result2, msg="断言失败")



if __name__ == '__main__':
    unittest.main()
