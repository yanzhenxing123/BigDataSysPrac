"""
@Author: yanzx
@Date: 2022/6/17 14:22
@Description: 
"""


from kafka import KafkaConsumer
# consumer = KafkaConsumer('sex', bootstrap_servers='172.18.0.2:9092')
consumer = KafkaConsumer('sex', bootstrap_servers='192.168.26.128:9092', api_version=(0, 10))
print("dadafa")
topics = consumer.topics()
print(topics)
for msg in consumer:
    print("dadafa")
    print((msg.value).decode('utf8'))
