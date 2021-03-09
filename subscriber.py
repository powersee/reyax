# create by powersee

import RPi.GPIO as GPIO
import paho.mqtt.client as mqtt
GPIO.setmode(GPIO.BCM)

# setting your username and password here
username = ""
password = ""
# your topic
# xx : Network_ID
topic = "api/command/xx/#"

# GPIO Num
ioNum = 21
GPIO.setwarnings(False)
GPIO.setup(ioNum, GPIO.OUT)

def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    client.subscribe(topic)

def on_message(client, userdata, msg):
    #print(msg.payload)
    result = str(msg.payload)
    if u"turnon" in result :
        GPIO.output(ioNum, GPIO.HIGH)
        print("on")
    elif u"turnoff" in result :
        GPIO.output(ioNum, GPIO.LOW)
        print("off")
    
client = mqtt.Client()
client.client_id = username + "0002"
client.username_pw_set(username,password)
client.on_connect = on_connect
client.on_message = on_message


client.connect("iot.reyax.com", 1883, 60)


client.loop_forever()

