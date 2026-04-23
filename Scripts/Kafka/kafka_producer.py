import pandas as pd
from kafka import KafkaProducer
from time import sleep
from json import dumps
import json

producer = KafkaProducer(bootstrap_servers=['54.87.201.83:9092'], #change ip here
                         value_serializer=lambda x: 
                         dumps(x).encode('utf-8'))

producer.send('kafka-project', value={'surnasdasdame':'parasdasdmar'}) # topic name

df = pd.read_csv("./data/indexProcessed.csv")

while True:
    dict_stock = df.sample(1).to_dict(orient="records")[0]
    producer.send('kafka-project', value=dict_stock) # topic name
    sleep(1)


