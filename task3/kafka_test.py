# coding: utf-8
from kafka import KafkaProducer
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
from pyspark import SparkConf, SparkContext
import json
import sys


def KafkaWordCount(zkQuorum, group, topics, numThreads):
    spark_conf = SparkConf().setAppName("KafkaWordCount")
    sc = SparkContext(conf=spark_conf)
    sc.setLogLevel("ERROR")
    ssc = StreamingContext(sc, 1)
    ssc.checkpoint(".")
    # 这里表示把检查点文件写入分布式文件系统 HDFS，所以要启动 Hadoop
    # ssc.checkpoint(".")
    topicAry = topics.split(",")
    # 将 topic 转换为 hashmap 形式，而 python 中字典就是一种 hashmap
    topicMap = {}
    for topic in topicAry:
        topicMap[topic] = numThreads
    lines = KafkaUtils.createStream(ssc, zkQuorum, group, topicMap).map(lambda x: x[1])
    words = lines.flatMap(lambda x: x.split(" "))
    wordcount = words.map(lambda x: (x, 1)).reduceByKeyAndWindow((lambda x, y: x + y), (lambda x, y: x - y), 1, 1,
                                                                 1)
    wordcount.foreachRDD(lambda x: sendmsg(x))

    ssc.start()
    ssc.awaitTermination()
    # 格式转化，将[["1", 3], ["0", 4], ["2", 3]]变为[{'1': 3}, {'0': 4}, {'2': 3}]，这样就不用修
    # 改第四个教程的代码了


def Get_dic(rdd_list):
    res = []

    for elm in rdd_list:
        tmp = {elm[0]: elm[1]}
        res.append(tmp)
    return json.dumps(res)


def sendmsg(rdd):
    if rdd.count != 0:
        msg = Get_dic(rdd.collect())

    # 实例化一个 KafkaProducer 示例，用于向 Kafka 投递消息
    # localhost 建议换为 hbase-master
    producer = KafkaProducer(bootstrap_servers='localhost:9092')
    producer.send("result", msg.encode('utf8'))
    # 很重要，不然不会更新
    producer.flush()


if __name__ == '__main__':
    # 输入的四个参数分别代表着
    # 1.zkQuorum 为 zookeeper 地址
    # 2.group 为消费者所在的组
    # 3.topics 该消费者所消费的 topics
    # 4.numThreads 开启消费 topic 线程的个数
    if (len(sys.argv) < 5):
        print("Usage: KafkaWordCount <zkQuorum> <group> <topics> <numThreads>")
        exit(1)
    zkQuorum = sys.argv[1]
    group = sys.argv[2]
    topics = sys.argv[3]
    numThreads = int(sys.argv[4])
    print(group, topics)
    KafkaWordCount(zkQuorum, group, topics, numThreads)
