import sqlite3
from database import init_db

def view_attendance():
    # Ensure database and table exist using your project's database module
    init_db()
    
    # Connect to the database file
    conn = sqlite3.connect('attendance.db')
    cursor = conn.cursor()
    
    # Query all rows from the attendance table
    cursor.execute('SELECT id, card_uid, timestamp FROM attendance')
    rows = cursor.fetchall()
    
    print("\n--- Attendance Records ---")
    if not rows:
        print("No attendance records found yet.")
    else:
        print(f"{'ID':<5} | {'Card UID':<15} | {'Timestamp'}")
        print("-" * 40)
        for row in rows:
            print(f"{row[0]:<5} | {row[1]:<15} | {row[2]}")
            
    conn.close()

if __name__ == "__main__":
    view_attendance()
