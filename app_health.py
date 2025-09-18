#!/usr/bin/env python3
import requests
import logging

# Setup logging
logging.basicConfig(filename="app_health.log",
                    level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")

# Application URL 
APP_URL = "http://google.com"

def check_app_health():
    try:
        response = requests.get(APP_URL, timeout=5)

        if response.status_code == 200:
            msg = f"Application is UP. Status Code: {response.status_code}"
            print(msg)
            logging.info(msg)
        else:
            msg = f"Application is DOWN. Status Code: {response.status_code}"
            print("ALERT:", msg)
            logging.warning(msg)

    except requests.exceptions.RequestException as e:
        msg = f"Application is DOWN. Error: {e}"
        print("ALERT:", msg)
        logging.error(msg)

if __name__ == "__main__":
    check_app_health()

