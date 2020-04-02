import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):  
    print("Connected with result code {0}".format(str(rc)))  
    client.subscribe("paho/test")  

def on_message(client, userdata, msg):  
    print("MQTT Received -> " + msg.topic + " " + str(msg.payload))  

client = mqtt.Client("subscribe")  
client.on_connect = on_connect  
client.on_message = on_message  

client.connect('52.80.49.162', 1883, 60)
client.loop_forever()
