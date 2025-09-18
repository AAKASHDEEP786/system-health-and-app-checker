#!/usr/bin/env python3
import psutil
import logging

# Setup logging
logging.basicConfig(filename="system_health.log",
                    level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")

# Thresholds
CPU_THRESHOLD = 80
MEM_THRESHOLD = 80
DISK_THRESHOLD = 80

def check_system_health():
    alerts = []

    # CPU usage
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > CPU_THRESHOLD:
        alerts.append(f"High CPU Usage: {cpu_usage}%")

    # Memory usage
    memory = psutil.virtual_memory()
    if memory.percent > MEM_THRESHOLD:
        alerts.append(f"High Memory Usage: {memory.percent}%")

    # Disk usage
    disk = psutil.disk_usage('/')
    if disk.percent > DISK_THRESHOLD:
        alerts.append(f"High Disk Usage: {disk.percent}%")

    # Running processes count
    processes = len(psutil.pids())
    if processes > 300:  # Example threshold
        alerts.append(f"Too many running processes: {processes}")

    # Print or log alerts
    if alerts:
        for alert in alerts:
            print("ALERT:", alert)
            logging.warning(alert)
    else:
        msg = "System health is normal."
        print(msg)
        logging.info(msg)

if __name__ == "__main__":
    check_system_health()

