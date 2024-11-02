import serial
import time
from datetime import datetime
import requests

ser = serial.Serial('/dev/ttyACM0', 9600)

SERVER_MONITOR_API_URL = "http://wovspi:<NodePort>/server-monitor/measurements"

def parse_sensor_data(line):
    try:
        # Check if the line contains both humidity and temperature
        if "Current humidity" in line and "temperature" in line:
            # Split by '=' and get the numbers
            parts = line.split("=")
            # Get humidity (middle part, remove %)
            humidity = float(parts[1].split("%")[0].strip())
            # Get temperature (last part, remove F)
            temperature = float(parts[2].split('F')[0].strip())

            return {
                "humidity": humidity,
                "temperature": temperature,
                "timestamp": datetime.now().isoformat()
            }
        return None

    except Exception as e:
        print(f"Error parsing line {line}: {str(e)}")
        return None

try:
    while True:
        line = ser.readline().decode('utf-8').strip()
        print(f"Received: {line}")

        data = parse_sensor_data(line)

        if data:
            try:
                response = requests.post(SERVER_MONITOR_API_URL, json=data)
                if response.status_code == 200:
                    print("Data sent successfully")
                else:
                    print(f"Error sending data: {response.status_code}")
            except requests.exceptions.RequestException as e:
                print(f"Failed to send data : {e}")
        time.sleep(5)

except KeyboardInterrupt:
    print("Exiting...")
    ser.close()