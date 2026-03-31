from kafka import KafkaConsumer

TOPIC_NAME = "testtopiic"

consumer = KafkaConsumer(
    TOPIC_NAME,
    bootstrap_servers=f"kafkapocdemo-wedotesthere-0001.k.aivencloud.com:10378",
    client_id = "CONSUMER_CLIENT_ID",
    group_id = "CONSUMER_GROUP_ID",
    security_protocol="SSL",
    ssl_cafile="ca.pem",
    ssl_certfile="service.cert",
    ssl_keyfile="service.key",
)

while True:
    for message in consumer.poll().values():
        print("Got message using SSL: " + message[0].value.decode('utf-8'))