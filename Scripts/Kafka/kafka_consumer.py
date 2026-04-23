from kafka import KafkaConsumer
from time import sleep
from json import dumps,loads
import json
from s3fs import S3FileSystem

consumer = KafkaConsumer(
    'kafka-project', # topic name
     bootstrap_servers=['54.87.201.83:9092'], #add your IP here
    value_deserializer=lambda x: loads(x.decode('utf-8')))

s3 = S3FileSystem(key='##', secret='##') #keys

for count, i in enumerate(consumer):
    with s3.open("s3://kafka-stock-market-mustafa/stock_market_{}.json".format(count), 'w') as file:
        json.dump(i.value, file) 

