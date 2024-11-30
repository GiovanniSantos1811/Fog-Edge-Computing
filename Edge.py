import requests
import random
import time

FOG_URL = "http://172.25.126.164:5000/process_data"  # Substitua pelo IP da máquina que executa fog.py

def generate_sensor_data():
    return {
        "temperature": random.uniform(20, 30),
        "humidity": random.uniform(40, 70)
    }

while True:
    data = generate_sensor_data()
    print(f"Sending data: {data}")
    try:
        response = requests.post(FOG_URL, json=data)
        print(f"Response: {response.json()}")
    except Exception as e:
        print(f"Error sending data: {e}")
    time.sleep(2)
