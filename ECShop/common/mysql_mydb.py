
import pymysql

class Database(object):

    def __init__(self,host="ecshop.itsoso.cn",
                 user="ecshop",
                 password="ecshop",
                 charset="utf8",
                 port=3306,
                 db="ecshop"):
        self.host=host
        self.user=user
        self.password=password
        self.charset=charset
        self.db=db
        self.port=port

        self.cn = pymysql.connect(host=self.host,
                                  user=self.user,
                                  password=self.password,
                                  charset=self.charset,
                                  port=self.port,
                                  db=self.db)
        self.cur=self.cn.cursor(cursor=pymysql.cursors.SSDictCursor)
    def read_one(self,sql,args=None):
        try:
            self.cur.execute(sql,args)
            #获取结果
            return self.cur.fetchone()
        except:
            print("无数据!")
            return False

    def read_all(self,sql,args=None):
            self.cur.execute(sql,args)
            return self.cur.fetchall()



    def write(self,sql,args=None):

        self.cn.begin()
        try:
            num=self.cur.execute(sql,args)
            if num==0:
                raise Exception("受影响 0 行!,操作失败")
            self.cn.commit()
            return True
        except Exception as e:
            # 回滚
            self.cn.rollback()
            print("错误信息: ",e)
            return False



if __name__ == '__main__':

    db=Database()
    sql="SELECT * FROM `ecs_user_address` where user_id=9608 "
    # result=db.read_one(sql)
    result = db.read_all(sql)
    result=result[0]['address_id']
    print(result)



    # db=Database()
    # args=[2]
    # sql="select * from student where id>%s"
    #
    # args=['xy',7]
    # sql2="update student set name=%s where id=%s"
    # result=db.read_all(sql2,args)
    # print(result)

    # db=Database()

    # sql="update student set name=%s where id=%s"
    # args = ["xxy", 7]
    # result=db.write(sql,args)
    # print(result)
    #


