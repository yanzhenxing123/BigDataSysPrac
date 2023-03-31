"""
@Author: yanzx
@Date: 2022/6/17 14:14
@Description: 
"""
# coding: utf-8
import csv
import time
from kafka import KafkaProducer


# 实例化一个 KafkaProducer 示例，用于向 Kafka 投递消息
producer = KafkaProducer(bootstrap_servers='hbase-master:9092')
# producer = KafkaProducer(bootstrap_servers='192.168.26.128:9092', api_version=(0, 10))
# 打开数据文件 user_log.csv 文件的位置

print("已连接")

# csvfile = open("/root/kafka_spark_code/user_log.csv","r")
# csvfile = open("./data/user_log.csv","r", encoding="utf-8")
# 生成一个可用于读取 csv 文件的 reader
# reader = csv.reader(csvfile)
print("已读取数据")
for line in range(1000):
    # gender = line[9] # 性别在每行日志代码的第 9 个元素
    # if gender == 'gender':
    #     continue # 去除第一行表头
    time.sleep(1) # 每隔 0.1 秒发送一行数据
    # 发送数据， topic 为 'sex'
    producer.send('sex',str(line).encode('utf8'))
    print("正在发送数据")
