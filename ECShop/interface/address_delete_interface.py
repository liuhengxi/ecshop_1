from common.send_method import SendMethod

from interface.login_interface import Login

class Del_address:
    '''
    移除收藏
    '''
    @staticmethod
    def del_address(del_collection_url,data):
        return SendMethod.send_method(del_collection_url,data)

if __name__ == '__main__':
    del_address_url="http://ecshop.itsoso.cn/ECMobile/?url=/address/delete"

    login = Login("http://ecshop.itsoso.cn/ECMobile/?url=/user/signin")
    login_data = {"name": "xxy", "password": "123456"}
    # print(login.login(login_data))
    session = login.get_session(login_data)
    address_data = {"address_id":"5695","session": session}
    print(Del_address.del_address(del_address_url,address_data))