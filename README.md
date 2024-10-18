# Personal Computer Health Monitor

This project uses the ELK (Elasticsearch, Logstash, Kibana) stack to monitor and visualize system metrics from your personal computer.

## Prerequisites

- Docker
- Docker Compose

## Setup and Run

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/elk-pc-monitor.git
   cd elk-pc-monitor
   ```

2. Start the ELK stack and metrics collector:
   ```
   docker-compose up -d
   ```

3. Open Kibana in your web browser:
   ```
   http://localhost:5601
   ```

4. In Kibana, go to Management > Stack Management > Index Patterns.
   Create a new index pattern with the pattern `pc-metrics-*`.

5. Go to Visualize and create new visualizations for CPU, Memory, and Disk usage.

6. Create a new Dashboard and add your visualizations to it.

## Stopping the Monitor

To stop the monitoring system:
```
docker-compose down
```

## Customization

You can modify the `metrics-collector/collect_metrics.py` script to collect additional metrics as needed.
