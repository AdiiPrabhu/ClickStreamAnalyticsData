import time
import json
import uuid
import random
from datetime import datetime, timezone
from kafka import KafkaProducer

TOPIC_NAME = "testtopiic"

producer = KafkaProducer(
    bootstrap_servers="kafkapocdemo-wedotesthere-0001.k.aivencloud.com:10378",
    security_protocol="SSL",
    ssl_cafile="ca.pem",
    ssl_certfile="service.cert",
    ssl_keyfile="service.key",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

pages = ["/", "/pricing", "/docs", "/signup", "/login", "/checkout", "/blog"]
actions = ["pageview", "click", "scroll", "signup"]
devices = ["mobile", "desktop", "tablet"]
browsers = ["Chrome", "Safari", "Firefox", "Edge"]
countries = ["IN", "US", "DE", "UK", "CA", "SG"]
referrers = ["google", "direct", "twitter", "linkedin", "ads"]

def generate_event():
    return {
        "event_id": str(uuid.uuid4()),
        "timestamp": datetime.now(timezone.utc).isoformat(),  # ISO 8601
        "user_id": f"user_{random.randint(1000, 9999)}",
        "session_id": f"sess_{random.randint(10000, 99999)}",
        "page": random.choice(pages),
        "referrer": random.choice(referrers),
        "action": random.choice(actions),
        "device": random.choice(devices),
        "browser": random.choice(browsers),
        "country": random.choice(countries),
        "duration_ms": random.randint(100, 5000)
    }

print(" Starting clickstream producer... Press Ctrl+C to stop.")

try:
    while True:
        event = generate_event()
        producer.send(TOPIC_NAME, value=event)
        print(f" Sent event: {event}")
        
        time.sleep(random.uniform(0.2, 1.0))

except KeyboardInterrupt:
    print("\n Stopping producer...")

finally:
    producer.flush()
    producer.close()