# Using a MQTT client to directly connect to IoT Hub

This is a simple example based on instuctions at https://docs.microsoft.com/en-us/azure/iot-hub/iot-hub-mqtt-support#using-the-mqtt-protocol-directly to connect a mqtt client directly to IoT Hub for bidirectional communication.

### Using the example

First you install the paho mqtt client using pip:

    pip install paho-mqtt

Then change the following variables:   

* For the **ClientId** field, use the **deviceId**.

* For the **Username** field, use `{iothubhostname}/{device_id}/api-version=2016-11-14`, where `{iothubhostname}` is the full CName of the IoT hub.

    For example, if the name of your IoT hub is **contoso.azure-devices.net** and if the name of your device is **MyDevice01**, the full **Username** field should contain:

    `contoso.azure-devices.net/MyDevice01/api-version=2016-11-14`

* For the **Password** field, use a SAS token. The format of the SAS token is the same as for both the HTTPS and AMQP protocols:

  `SharedAccessSignature sig={signature-string}&se={expiry}&sr={URL-encoded-resourceURI}`

  When testing, you can also use the [device explorer][lnk-device-explorer] tool to quickly generate a SAS token that you can copy and paste into your own code:

  1. Go to the **Management** tab in **Device Explorer**.
  2. Click **SAS Token** (top right).
  3. On **SASTokenForm**, select your device in the **DeviceID** drop down. Set your **TTL**.
  4. Click **Generate** to create your token.

     The SAS token that's generated has the following structure:

     `HostName={your hub name}.azure-devices.net;DeviceId=javadevice;SharedAccessSignature=SharedAccessSignature sr={your hub name}.azure-devices.net%2Fdevices%2FMyDevice01%2Fapi-version%3D2016-11-14&sig=vSgHBMUG.....Ntg%3d&se=1456481802`

     The part of this token to use as the **Password** field to connect using MQTT is:

     `SharedAccessSignature sr={your hub name}.azure-devices.net%2Fdevices%2FMyDevice01%2Fapi-version%3D2016-11-14&sig=vSgHBMUG.....Ntg%3d&se=1456481802`


### Subscribing cloud-to-device messages

To receive messages from IoT Hub, a device should subscribe using `devices/{device_id}/messages/devicebound/#` as a **Topic Filter**. The multi-level wildcard `#` in the Topic Filter is used only to allow the device to receive additional properties in the topic name. IoT Hub does not allow the usage of the `#` or `?` wildcards for filtering of subtopics. Since IoT Hub is not a general-purpose pub-sub messaging broker, it only supports the documented topic names and topic filters.

