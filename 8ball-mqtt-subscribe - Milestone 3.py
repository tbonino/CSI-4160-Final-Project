import paho.mqtt.client as mqtt

# The callback function of connection
# (This gets called once we're connected to the MQTT broker)
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    client.subscribe("8_ball") # subscribe to "8_ball"

# The callback function for received message
# (This gets called each time a message is recieved from our subscription to "my_topic")
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1)
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set("user", "test123")
client.connect("35.226.151.26", 1883, 60)
client.loop_forever()
