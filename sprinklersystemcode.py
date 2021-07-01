import time
import sys
import ibmiotf.application
import ibmiotf.device
import random
import json

#Provide your IBM Watson Device Credentials
organization = "x8sfnd"
deviceType = "iotdevice"
deviceId = "1001"
authMethod = "token"
authToken = "1234567890"


# Initialize the device client.
W=0
S=0

def myCommandCallback(cmd):
        print("Command received: %s" % cmd.data['command'])


        if cmd.data['command']=='sprinkleron':
                print("Sprinkler ON IS RECEIVED")
                
                
        elif cmd.data['command']=='sprinkleroff':
                print("Sprinkler OFF IS RECEIVED")
        
      
try:
	deviceOptions = {"org": organization, "type": deviceType, "id": deviceId, "auth-method": authMethod, "auth-token": authToken}
	deviceCli = ibmiotf.device.Client(deviceOptions)
	#..............................................
	
except Exception as e:
	print("Caught exception connecting device: %s" % str(e))
	sys.exit()

# Connect and send a datapoint "hello" with value "world" into the cloud as an event of type "greeting" 10 times
deviceCli.connect()

while True:
        W=89
        S=44
        #Send Temperature & Humidity to IBM Watson
        data = jsondata={"d":{ 'water level' : W, 'soil moisture':S }}
        print (data)
        
        def myOnPublishCallback():
            print ("Published Water Level = %s units"% W, "Soil moisture = %s %%" % S, "to IBM Watson")

        success = deviceCli.publishEvent("Data", "json", data, qos=0, on_publish=myOnPublishCallback)
        if not success:
            print("Not connected to IoTF")
        time.sleep(1)
        
        deviceCli.commandCallback = myCommandCallback

# Disconnect the device and application from the cloud
deviceCli.disconnect()
