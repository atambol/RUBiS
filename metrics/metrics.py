import psutil
import time
from kafka import KafkaProducer
from kafka.errors import KafkaError


def get_stats():
    epoch = str(int(time.time()))
    cpu = str(int(psutil.cpu_percent(interval=1)))
    mem = str(int(psutil.virtual_memory().percent))
    return ",".join([epoch, cpu, mem])


def main():
    producer_topic = 'cpu'
    bootstrap_servers = '172.25.130.9:9092'
    producer = KafkaProducer(bootstrap_servers=[bootstrap_servers])
    while True:
        future = producer.send(producer_topic, get_stats())
        # Block for 'synchronous' sends
        try:
            future.get(timeout=10)
        except KafkaError as err:
            print err


if __name__ == "__main__":
    main()
