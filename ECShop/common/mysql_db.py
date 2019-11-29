from pymysql import cursors, connect
from pymysql.err import OperationalError
import os
import configparser as cparser
from common.operartion_Excel import Operationxcel

# =====================读取db_config.ini文件设置
base_dir = str(os.path.dirname(os.path.dirname(__file__)))
base_dir = base_dir.replace('\\', '/')
file_path = base_dir + '/common/db_config.ini'

cf = cparser.ConfigParser()
cf.read(file_path)

host = cf.get('mysqlconf', 'host')
port = cf.get('mysqlconf', 'port')
user = cf.get('mysqlconf', 'user')
password = cf.get('mysqlconf', 'password')
db = cf.get('mysqlconf', 'db_name')


# ======================封装mysql
class DB(object):

    def __init__(self):
        try:
            self.conn = connect(host=host,
                                user=user,
                                password=password,
                                db=db,
                                charset='utf8mb4',
                                cursorclass=cursors.DictCursor)
        except OperationalError as e:
            print("mysql Error %d :%s" % (e.args[0], e.args[1]))

    def clear(self, table_name):
        # real_sql='truncate table'+table_name+';'
        real_sql = 'delete from ' + table_name + ';'
        with self.conn.cursor() as cursor:
            cursor.execute('SET FOREIGN_KEY_CHECKS=0;')
            cursor.execute(real_sql)
        self.conn.commit()

    def insert(self, table_name, table_data):
        for key in table_data:
            table_data[key] = "'" + str(table_data[key]) + "'"
        key = ','.join(table_data.keys())
        value = ','.join(table_data.values())
        real_sql = 'insert into ' + table_name + '(' + key + ') values(' + value + ');'
        print(real_sql)
        with self.conn.cursor() as cursor:
            cursor.execute(real_sql)
        self.conn.commit()

    def read_one(self, key,value,table_data=None, table_name='*'):
        read_sql = 'select '+ table_name + ' from  '+table_data  +' where '+ key + '=' + value +';'
        with self.conn.cursor() as cursor:
            cursor.execute(read_sql)
            return cursor.fetchone()
    def delete_all(self,table_name,table,value):
        real_sql = 'delete from '  +  table_name  + ' where '+ table + ' = ' + value+';'
        with self.conn.cursor() as cursor:
            cursor.execute('SET FOREIGN_KEY_CHECKS=0;')
            cursor.execute(real_sql)
        self.conn.commit()

    def read_all(self, key,value,table_data=None, table_name='*'):
        read_sql = 'select '+ table_name + ' from  '+table_data  +' where '+ key + '=' + value +';'
        with self.conn.cursor() as cursor:
            cursor.execute(read_sql)
            return cursor.fetchall()

    def close(self):
        self.conn.close()


if __name__ == '__main__':
    db = DB()

    # db.delete_all('ecs_users','user_id','9683')
    # print(db.read_all('address_id','100000','ecs_user_address'))
    # print(db.read_all("goods_id", '89', "ecs_goods"))
    print(db.read_all("user_id", "9310", "ecs_cart", 'goods_id'))








