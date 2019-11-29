from common.send_method import SendMethod
from common.get_result import GetKeyword
from interface.login_interface import Login


class Colection:
    @staticmethod
    def get_colection(url,data):
        return SendMethod.send_method(url,data)

if __name__ == '__main__':
    get_colection_url = "http://ecshop.itsoso.cn/ECMobile/?url=/user/collect/list"  # 地址列表网址

    login = Login("http://ecshop.itsoso.cn/ECMobile/?url=/user/signin")  # 登录

    login_data = {"name": "xxy", "password": "123456"}  # 登录数据

    session = login.get_session(login_data)  # 获取登录后session

    address_data = {"session": session}  # 查看收货地址请求参数

    print(Colection.get_colection(get_colection_url, address_data))


