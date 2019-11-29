from common.send_method import SendMethod

from interface.login_interface import Login

class Update_address:
    '''
    添加收藏
    '''
    @staticmethod
    def update_address(add_collection_url,data):
        return SendMethod.send_method(add_collection_url,data)

if __name__ == '__main__':
    update_address_url = "http://ecshop.itsoso.cn/ECMobile/?url=/address/update"

    login = Login("http://ecshop.itsoso.cn/ECMobile/?url=/user/signin")   #登录

    login_data = {"name": "xxy", "password": "123456"}
    # print(login.login(login_data))
    session =login.get_session(login_data)
    address_data = {"address":{"default_address":0,"consignee":"user",
                               "tel":"1898976579464","zipcode":"621000",
                               "country":"4044","city":"0","id":0,
                               "email":"98784564@qq.com","address":"*********",
                               "province":"0","district":"0","mobile":""},"address_id":"5698","session": session}
    print(Update_address.update_address(update_address_url, address_data))
