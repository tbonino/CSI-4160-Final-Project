# see notes:
# https://www.emqx.com/en/blog/comparision-of-python-mqtt-client
# https://techoverflow.net/2021/12/27/how-to-set-username-password-in-paho-mqtt/

import paho.mqtt.client as mqtt
import time
import magic8ball

def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1)
client.on_connect = on_connect

# If you forget the following line (or the user/pass is wrong) then you might get
# "Connected with result code 5" which means authentication failure
client.username_pw_set("bonino4160", "test123")

client.connect("35.226.151.26", 1883, 60)

#load payload variable
#r = magic8ball.get_web_reply()

# send 3 messages
#for i in range(1):
while(True):
    r = magic8ball.get_web_reply()
    my_payload = "Magic 8 Ball Result: " + str(r)
    client.publish('8_ball', payload=my_payload, qos=0, retain=False)
    print(f"publishing '{my_payload}' to '8_ball'")
    time.sleep(1)

client.loop_forever()
