from confluent_kafka import Consumer, KafkaError

# Kafka broker settings
bootstrap_servers = 'localhost:9092'
topic = 'topic-game'
group_id = 'your_consumer_group_id'

# Create consumer configuration
conf = {
    'bootstrap.servers': bootstrap_servers,
    'group.id': group_id,
    'auto.offset.reset': 'earliest'  # start reading at the earliest available offset
}

# Create Kafka consumer
consumer = Consumer(conf)

# Subscribe to topic(s)
consumer.subscribe([topic])

# Poll for new messages
try:
    while True:
        msg = consumer.poll(timeout=1.0)
        if msg is None:
            continue
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                continue
            else:
                print(msg.error())
                break
        print('Received message: {}'.format(msg.value().decode('utf-8')))
except KeyboardInterrupt:
    pass
finally:
    # Close the consumer on exit
    consumer.close()
