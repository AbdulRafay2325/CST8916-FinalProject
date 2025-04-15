from azure.iot.device.aio import IoTHubDeviceClient
from dotenv import load_dotenv

import time
import os
import json
import asyncio
import datetime
import random

# Load environment variables from .env file (if it exists)
load_dotenv()

# Connection strings directly from your last provided code
connectionStrings = [
    os.getenv('IOTHUB_STR1') or "HostName=FinalProject.azure-devices.net;DeviceId=Sensor1IoT;SharedAccessKey=/W3E5cPCLkXrBkNM+4CkDCGjchPi42GbL5xr1tyuT+Q=",
    os.getenv('IOTHUB_STR2') or "HostName=FinalProject.azure-devices.net;DeviceId=Sensor2IoT;SharedAccessKey=qKiXGiZEoQbLnONVz944SqMB3XjQKuuoAFQUN/thgiA=",
    os.getenv('IOTHUB_STR3') or "HostName=FinalProject.azure-devices.net;DeviceId=Sensor3IoT;SharedAccessKey=V2rBNld7i7lOjjuXDDyWxFMdnod4EsYSNQxXRqbNOu8="
]

# Check if connection strings are available
if all(connectionStrings):
    print("Connection Strings:")
    for i, conn in enumerate(connectionStrings):
        print(f"Sensor {i+1}: {conn}")
else:
    print("Error: Not all connection strings are available. Please ensure they are either in the .env file or directly in the code.")
    exit()

async def sendToIotHub(data, conn_index):
    try:
        # Create an instance of the IoT Hub Client class
        deviceId = IoTHubDeviceClient.create_from_connection_string(connectionStrings[conn_index])

        # Connect to client
        await deviceId.connect()

        # Send message
        await deviceId.send_message(data)
        print("Message sent to IoT Hub:", data)

        # Shutdown client
        await deviceId.shutdown()

    except Exception as e:
        print("Error sending to IoT Hub:", str(e))

def main():
    # Run an infinite while loop to send data
    while True:
        # Generate random value
        locations = ["Dow's Lake", "Fifth Avenue", "NAC"]

        # Generate data for each location
        for i, location in enumerate(locations):
            iceThickness = random.randrange(0, 10) # generates a random num between 0 and 10
            surfaceTemp = random.randrange(-30, 10) # generates a random num between -30 and 10 for temp
            snowAccumulation = random.randrange(0, 10) # generates a random num between 0 and 10
            externalTemp = random.randrange(-30, 10) # generates a random number between -30 and 10

            msgData={ # pass the generated variables to an object
                "location": location,
                "iceThickness": iceThickness,
                "surfaceTemperature": surfaceTemp,
                "snowAccumulation": snowAccumulation,
                "externalTemperature": externalTemp,
                "timestamp":str(datetime.datetime.now())
            }
            # the following runs an asynchronous task and passing the payload
            asyncio.run(sendToIotHub(data=json.dumps(msgData), conn_index=i))
            time.sleep(10)

if __name__ == '__main__':
    main()
