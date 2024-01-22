from kafka import KafkaProducer
import time
import logging


def kafka_producer():
    producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                             max_block_ms=5000)
    
    
    curr_time = time.time()
    
    while time.time() > curr_time + 60:
        try:
            producer.send('test', b'Hello, World!')
            
            print('Message published successfully.')
            
        except Exception as ex:
            logging.error('Exception while publishing message to Kafka %s', ex)
            continue



if __name__ == '__main__':
    kafka_producer()