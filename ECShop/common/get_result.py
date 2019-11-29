import jsonpath
# 封装获取接口返回值方法
class GetKeyword:
    @staticmethod
    def get_keyword(response:dict,keyword):
        """
        通过关键字获取对应返回值,如果有多个值,只返回第一个,如果关键字不存在,返回False
        :param:response 数据源  字典格式
        :param:keyword 要获取的字段
        :return:
        """
        try:
            return jsonpath.jsonpath(response,f"$..{keyword}")[0]
        except:
            print("关键字不存在")
            return False

    @staticmethod
    def get_keywords(response:dict,keyword):
        """
        通过关键字获取一组数据
        :param response: 数据源 dict格式
        :param keyword:  如果关键字不存在,返回False
        :return:
        """
        return jsonpath.jsonpath(response,f"$..{keyword}")
