from confluent_kafka import Producer

# Kafka broker settings
bootstrap_servers = 'localhost:9092'
topic = 'topic-game'
partition = 0  # Specify the partition number
message_key = 'your_key'  # Specify a key for message partitioning

# Create producer configuration
conf = {'bootstrap.servers': bootstrap_servers}

# Create Kafka producer
producer = Producer(conf)

# Define a delivery report callback function
def delivery_callback(err, msg):
    if err:
        print('Message delivery failed: {}'.format(err))
    else:
        print('Message delivered to topic [{}] partition [{}]'.format(msg.topic(), msg.partition()))

# Produce message with specified partition key
message_value = "test"
while(True):
# partition = int(input("Enter partition number"))
    message = input("Enter message")
    if (len(message)>5):
        partition = 1
    if message is None:
        message = message_value    
    producer.produce(topic, key=message_key, value=message, partition=partition, callback=delivery_callback)

    # Wait for the message to be delivered
    producer.flush()

    # Close the producer
producer = None
