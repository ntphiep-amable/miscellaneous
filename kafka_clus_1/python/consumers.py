import json
from kafka import KafkaConsumer

consumer = KafkaConsumer(
    'test',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
)

for message in consumer:
    message = message.value.decode('utf-8')
    message = json.loads(message)
    print(message)