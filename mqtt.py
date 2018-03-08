from paho.mqtt import client as mqtt
import ssl

path_to_root_cert = "cert.cer"
device_id = "test"
sas_token = "SharedAccessSignature sr=mqconnector.azure-devices.net%2Fdevices%2Ftest&sig=HM%2FVq2GpBN5j5xFCq60Gw8VrxQiSjtBFRwAD%2BuA1nBg%3D&se=1523137214"
iot_hub_name = "mqconnector"

def on_connect(client, userdata, flags, rc):
  print ("Device connected with result code: " + str(rc))
def on_disconnect(client, userdata, rc):
  print ("Device disconnected with result code: " + str(rc))
def on_publish(client, userdata, mid):
  print ("Device sent message")
def on_message(client, userdata, msg):
    print("Message received at: " + msg.topic+" with payload: "+str(msg.payload))

client = mqtt.Client(client_id=device_id, protocol=mqtt.MQTTv311)

client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_publish = on_publish
client.on_message = on_message

client.username_pw_set(username=iot_hub_name+".azure-devices.net/" + device_id, password=sas_token)

client.tls_set(ca_certs=path_to_root_cert, certfile=None, keyfile=None, cert_reqs=ssl.CERT_REQUIRED, tls_version=ssl.PROTOCOL_TLSv1, ciphers=None)
client.tls_insecure_set(False)

client.connect(iot_hub_name+".azure-devices.net", port=8883)

client.publish("devices/" + device_id + "/messages/events/", "{id=123}", qos=1)
client.subscribe("devices/" + device_id + "/messages/devicebound/#")

client.loop_forever()