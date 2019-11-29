import pandas
class Operationxcel:
    def __init__(self,filename):
        self.table =pandas.read_excel(filename)#通过pandas读取excel表格
    def get_data_info(self):
        """
        将读取的数据转化成列表嵌套字典格式[{},{}]
        :return:
        """
        data=[]
        for i in self.table.index.values:#遍历表格中的行数
            raw_data=self.table.loc[i].to_dict()#将每一行的内容转化为字典
            data.append(raw_data)#将转化后的内容添加到空列表

        return data


