import serial
import time

# Update '/dev/ttyUSB0' if your ESP32 port is different (e.g., /dev/ttyACM0)
PORT = "/dev/ttyUSB0"
BAUD = 115200

print(f"Connecting to ESP32 on {PORT}...")

try:
    ser = serial.Serial(PORT, BAUD, timeout=1)
    time.sleep(2)  # Allow connection to settle
    print("Connected! Waiting for RFID cards...")

    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode("utf-8").strip()
            print(f"Received: {line}")
except Exception as e:
    print(f"Error: {e}")