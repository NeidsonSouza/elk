import time
import psutil
import socket
from datetime import datetime
from logstash import TCPLogstashHandler

def collect_metrics():
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent

    return {
        'timestamp': datetime.now().isoformat(),
        'cpu_usage': cpu,
        'memory_usage': memory,
        'disk_usage': disk
    }

def main():
    logger = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    logger.connect(('logstash', 5000))

    while True:
        metrics = collect_metrics()
        logger.send(str(metrics).encode() + b'\n')
        time.sleep(5)

if __name__ == "__main__":
    main()
