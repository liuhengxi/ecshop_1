from common.send_method import SendMethod

from interface.login_interface import Login

class Del_collection:
    '''
    移除收藏
    '''
    @staticmethod
    def del_collection(del_collection_url,data):
        return SendMethod.send_method(del_collection_url,data)

if __name__ == '__main__':
    del_collection_url="http://ecshop.itsoso.cn/ECMobile/?url=/user/collect/delete"

    login = Login("http://ecshop.itsoso.cn/ECMobile/?url=/user/signin")
    login_data = {"name": "xxy", "password": "123456"}
    # print(login.login(login_data))
    session = login.get_session(login_data)
    address_data = {"session": session, "rec_id":"2665"}
    print(Del_collection.del_collection(del_collection_url,address_data))