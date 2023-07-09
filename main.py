import paho.mqtt.client as mqtt
import ssl
import json
import _thread
import time
from datetime import datetime

broker = "a1vs29u7y7oh8s-ats.iot.eu-west-1.amazonaws.com"
caPath = "./AmazonRootCA1.pem"
certPath = "./certificate.pem.crt"
keyPath = "./private.pem.key"
topic = "sesnor/temp"

def on_connect(client, userdata, flags, rc):
    print("Connected to AWS IoT: " + str(rc))

client = mqtt.Client()
client.on_connect = on_connect
client.tls_set(ca_certs=caPath, certfile=certPath, 
               keyfile=keyPath, tls_version=ssl.PROTOCOL_SSLv23)
client.tls_insecure_set(True)
client.connect(broker, 8883, 60)


def publishData():
     
    while (True):
        timestamp = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
        data = json.dumps({"timestamp": timestamp,
                           "device_id":"sensor-1", 
                           "tempC": 10})
        client.publish(topic, payload=data,qos=0, retain=False)
        print("published")
        time.sleep(5)
        
_thread.start_new_thread(publishData,())

client.loop_forever()





