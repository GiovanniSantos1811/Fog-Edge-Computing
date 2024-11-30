import requests
import random
import time

FOG_URL = "http://192.168.118.139:5000/process_data" #Endereço do FOG, para que possamos nos conectar
UPPER_LIM = 70 #Limite máximo aceitável para o nível de vibração de uma máquina - acima disso precisa de manutenção

def generate_sensor_data():
    return {
        "sensor_id": random.randint(1, 10), #Id definido para cada sensor
        "sensor_data": random.uniform(0.0, 100.0) #Gerando um dado de sensor, o qual corresponde ao nível de vibração de uma máquina
    }

while True:
    data = generate_sensor_data() 

    print("Sensor com id ", data["sensor_id"], ", tem nível de vibração de ", data["sensor_data"])

    if (data["sensor_data"] > UPPER_LIM): #Ultrapassou o limite - envia para a fog
        print("Nível problemático. Enviando para FOG!")
        try:
            requests.post(FOG_URL, json=data)
        except Exception as e:
            print(f"Erro ao enviar dado: {e}")
    else:
        print("Nível aceitável.")

    time.sleep(2)

