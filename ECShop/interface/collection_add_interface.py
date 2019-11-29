from common.send_method import SendMethod

from interface.login_interface import Login

class Add_collection:
    '''
    添加收藏
    '''
    @staticmethod
    def add_collection(add_collection_url,data):
        return SendMethod.send_method(add_collection_url,data)

if __name__ == '__main__':
    add_collection_url = "http://ecshop.itsoso.cn/ECMobile/?url=/user/collect/create"

    login = Login("http://ecshop.itsoso.cn/ECMobile/?url=/user/signin")   #登录

    login_data = {"name": "xxy", "password": "123456"}
    # print(login.login(login_data))
    session =login.get_session(login_data)
    address_data = {"session": session,"goods_id":68}
    print(Add_collection.add_collection(add_collection_url, address_data))
