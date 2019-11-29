from common.send_method import SendMethod
from common.get_result import GetKeyword
from interface.login_interface import Login


class Address:
    @staticmethod
    def get_address(url,data):
        return SendMethod.send_method(url,data)

if __name__ == '__main__':
    get_address_url = "http://ecshop.itsoso.cn/ECMobile/?url=/address/list"  # 地址列表网址

    login = Login("http://ecshop.itsoso.cn/ECMobile/?url=/user/signin")  # 登录
    login_data = {"name": "xxy", "password": "123456"}  # 登录数据
    session = login.get_session(login_data)  # 获取登录后session
    # print(session)
    address_data = {"session": session}  # 查看收货地址请求参数
    print(Address.get_address(get_address_url, address_data))
    print("*"*60)
    #  self.login.get_status(self.login_data)['succeed']
    print(login.get_addrid(login_data))
