import time
import random

while True:
    temp = round(random.uniform(20, 80), 2)
    voltage = round(random.uniform(3.0, 5.0), 2)
    timestamp = time.ctime()
    with open("device_log.txt", "a") as f:
        f.write(f"{timestamp}, Temp: {temp}°C, Voltage: {voltage}V\n")
    time.sleep(5)  # simulate reading every 5 seconds
