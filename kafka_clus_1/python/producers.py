from kafka import KafkaProducer
import datetime
from gen_data import generate_message
import json

def serialize(message):
    return json.dumps(message).encode('utf-8')


producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=serialize,
)

if __name__ == "__main__":
    for i in range(100):
        dummy_message = generate_message()
        
        # Send it to our 'messages' topic
        print(f'Producing message @ {datetime.now()} | Message = {str(dummy_message)}')
        producer.send('messages', dummy_message)
        
        # Sleep for a random number of seconds