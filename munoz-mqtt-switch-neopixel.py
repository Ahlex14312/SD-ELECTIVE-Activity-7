from adafruit_circuitplayground import cp
import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc): # is used for checking that the connection was established 
    if rc == 0: #if the rc is equal to 0
        cp.red_led = True # the led in index 0 will on/light 
        client.subscribe("switch/#") # find the the published topic

def on_message(client, userdata, msg): #is used for checking published topic is subscribe  
    if msg.topic=="switch/switch0": #if the topic is equal to the subscribe topic in which the switch 0 is on 
        if msg.payload.decode() == "true": #and the msg.payload.decode is equal
            cp.pixels[0] = (255, 0, 0) #the pixel 0 will turn on in red color
        else: #if not
            cp.pixels[0] = (0, 0, 0) #the pixel 0 is off
    elif msg.topic=="switch/switch1": #if the topic is equal to the subscribe topic in which the switch 1 is on 
        if msg.payload.decode() == "true":#and the msg.payload.decode is equal
            cp.pixels[1] = (0, 255, 0)#the pixel 1 will turn on in green color
        else:
            cp.pixels[1] = (0, 0, 0)#the pixel 0 is off
    elif msg.topic=="switch/switch2": #if the topic is equal to the subscribe topic in which the switch 2 is on 
        if msg.payload.decode() == "true":#and the msg.payload.decode is equal
            cp.pixels[2] = (0, 0, 255) #the pixel 2 will turn on in blue color
        else:
            cp.pixels[2] = (0, 0, 0)#the pixel 0 is off
cp.red_led = False

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("test.mosquitto.org", 1883, 60) #connection address

client.loop_forever()

# Broker for online client: https://iamelijah2016.github.io/
# wss://mqtt.eclipse.org:443/mqtt
# wss://test.mosquitto.org:8081/mqtt