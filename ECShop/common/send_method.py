"""
接口文档编写,ecshop项目接口特点
请求方式:POST
请求参数:urlencoded
请求参数:json:参数值
"""
import requests
import json
class SendMethod:
    @staticmethod
    def send_method(url,data=None):
        # request_data={"json":json.dumps(data)}
        response=requests.post(url=url,data={"json":json.dumps(data)})
        return response.json()
if __name__ == '__main__':
    pass