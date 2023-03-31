import pymysql
class Mysql(object):
    def __init__(self):
        try:
            self.conn = pymysql.connect(host='192.168.26.128',user='root',password='hadoop',database='graph',port=3306, charset="utf8")
            self.cursor = self.conn.cursor()  # 用来获得python执行Mysql命令的方法（游标操作）
            print("连接数据库成功")
        except:
            print("连接失败")

    def getItems1(self):
        sql= "select * from topicDist order by cnt desc limit 10"    #获取网络主要主题的频率
        self.cursor.execute(sql)
        items1 = self.cursor.fetchall()  #接收全部的返回结果行
        print(items1)
        return items1

    def getItems2(self):
        sql = "select * from cooccurs order by cnt desc limit 10"  # 获取伴生二元组数据表的内容
        self.cursor.execute(sql)
        items2 = self.cursor.fetchall()  # 接收全部的返回结果行
        print(items2)
        return items2

    def getItems3(self):
        sql = "select * from name_degree order by degree desc limit 10"  # 获取初始图中度数最高的10个顶点
        self.cursor.execute(sql)
        items3 = self.cursor.fetchall()  # 接收全部的返回结果行
        print(items3)
        return items3
    def getItems4(self):
        sql = "select * from filter_degree order by degree desc limit 10"  # 获取过滤后图中度数最高的10个顶点
        self.cursor.execute(sql)
        items4 = self.cursor.fetchall()  # 接收全部的返回结果行
        print(items4)
        return items4


