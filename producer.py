from faker import Faker
import time
from kafka import KafkaProducer
import json

fake = Faker()

def get_registered_user():
    return {
        "name" : fake.name(),
        "address": fake.address(),
        "created_at":fake.time()
    }

def json_serializer(data):
    return json.dumps(data).encode("utf-8")

producer = KafkaProducer(bootstrap_servers = ["localhost:9092","localhost:9093","localhost:9094"], value_serializer=json_serializer)


if __name__ == "__main__":
    while True:
        get_data = get_registered_user()
        print(get_data)
        producer.send("user_data", get_data)
        time.sleep(5)