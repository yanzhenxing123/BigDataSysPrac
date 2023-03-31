from kafka import KafkaConsumer
#consumer = KafkaConsumer('sex', bootstrap_servers='172.18.0.2:9092',  api_version=(0, 10))
# consumer = KafkaConsumer('stream-topic', bootstrap_servers='192.168.26.128:9092', api_version=(0, 10))
consumer = KafkaConsumer('sex', bootstrap_servers='192.168.26.128:9092', api_version=(0, 10))
print("已连接")
for msg in consumer:
    print((msg.value).decode('utf8'))
