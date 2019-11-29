"""
test_login.py文件
    1.封装页面业务:对页面上面多个元素操作后所实现的功能
    2.测试用例
"""

from interface.login_interface import Login
from interface.collection_get_interface import Colection
import ddt,unittest
import time


from common.operartion_Excel import Operationxcel
#准备测试数据
oper = Operationxcel('./datas/getCollection_data.xls')
login_data = oper.get_data_info()

@ddt.ddt
class TextLogin(unittest.TestCase):
    def setUp(self) -> None:
        self.url="http://ecshop.itsoso.cn/ECMobile/?url=/user/signin"
        self.get_colection_url="http://ecshop.itsoso.cn/ECMobile/?url=/user/collect/list"

    def tearDown(self) -> None:
        # 关闭浏览器
        time.sleep(1)

    @ddt.data(*login_data)
    def test_login(self,data):
        self.login = Login(self.url)
        self.login_data = {"name": str(data["name"]), "password": str(data["password"])}
        # print(self.login_data)
        # print(self.login.login({"name": str(data["name"]), "password": str(data["password"])}))

        self.session = self.login.get_session(self.login_data)  # 获取登录后session

        self.address_data = {"session": self.session}  # 查看收货地址请求参数

        self.info = Colection.get_colection(self.get_colection_url, self.address_data)
        print(self.info)#打印收藏信息

        # 断言是否成功
        self.assertEqual(1, self.login.get_status_new(self.info)['succeed'], msg="断言失败")



if __name__ == '__main__':
    unittest.main()
