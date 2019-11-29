from common.send_method import SendMethod
from common.get_result import GetKeyword
class Login:
    def __init__(self,url):
        self.url=url
    def login(self,data):
        return SendMethod.send_method(self.url,data)
    def get_session(self,data):
        """
        获取登录之后的session
        :param url:
        :param data:
        :return:
        """
        res = self.login(data)
        return GetKeyword.get_keyword(res, "session")
    def get_succeed(self,data):
        """
        判定是否成功
        :param data:
        :return:
        """
        res=self.login(data)
        return GetKeyword.get_keyword(res, "succeed")
    def get_login_uid(self,data):
        """获取uid"""
        res=self.login(data)
        return GetKeyword.get_keyword(res,"uid")
    def get_login_session(self,data):
        """获取session"""
        res=self.login(data)
        return GetKeyword.get_keyword(res,"session")
    def get_addrids(self,res):
        """获取登录后的session"""

        return GetKeyword.get_keywords(res,"id")
    def get_status_new(self,res):
        """获取登录后的session"""
        return GetKeyword.get_keyword(res,"status")
    def get_addrid(self,res):
        """获取登录后的session"""

        return GetKeyword.get_keyword(res,"id")
    def get_rec_id(self,res):
        """获取登录后的session"""

        return GetKeyword.get_keywords(res,"rec_id")
    # def get_login_sid(self,data):
    #     """获取sid"""
    #     res = self.login(data)
    #     return GetKeyword.get_keyword(res, "sid")
if __name__ == '__main__':
    url = "http://ecshop.itsoso.cn/ECMobile/?url=/user/signin"
    login = Login(url)
    login_data = {"name": "Jerry", "password": "Test123456"}
    # print(login.login(login_data))
    # print(login.get_succeed(login_data))
    print(login.get_login_uid(login_data))