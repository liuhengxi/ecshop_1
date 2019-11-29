from common.send_method import SendMethod

from interface.login_interface import Login

class Add_collection:
    '''
    添加收藏
    '''
    @staticmethod
    def add_address(add_collection_url,data):
        return SendMethod.send_method(add_collection_url,data)

if __name__ == '__main__':
    add_address_url = "http://ecshop.itsoso.cn/ECMobile/?url=/address/add"

    login = Login("http://ecshop.itsoso.cn/ECMobile/?url=/user/signin")   #登录

    login_data = {"name": "xxy", "password": "123456"}
    # print(login.login(login_data))
    session =login.get_session(login_data)
    address_data = {"address":{"default_address":0,"consignee":"zzc",
                               "tel":"18080263593","zipcode":"621000",
                               "country":"4044","city":"",
                               "id":0,"email":"xxxx@qq.com",
                               "address":"我我我我我我我","province":"",
                               "district":"","mobile":""},"session": session}
    print(Add_collection.add_address(add_address_url, address_data))
