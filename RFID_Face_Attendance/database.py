import serial
import time
from database import init_db, log_attendance

# Initialize the database table
init_db()

# Adjust port if needed based on your setup
SERIAL_PORT = '/dev/ttyUSB0'
BAUD_RATE = 9600

print(f"Connecting to ESP32 on {SERIAL_PORT}...")
ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
time.sleep(2) # Allow connection to settle

print("Connected! Waiting for RFID cards...")

try:
    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').strip()
            if line:
                print(f"Received: {line}")
                
                # Check for the card UID pattern from your ESP32
                if "Card UID:" in line:
                    card_uid = line.split("Card UID:")[-1].strip()
                    # Log the scan with a timestamp into SQLite
                    log_attendance(card_uid)
                    
        time.sleep(0.1)
except KeyboardInterrupt:
    print("\nExiting program.")
    ser.close()