import threading
from datetime import datetime

class Logger:
    def __init__(self, log_file='log.txt'):
        """ตั้งค่าชื่อไฟล์ log"""
        self.log_file = log_file

    def log(self, msg):
        """ฟังก์ชันเพื่อแสดงข้อความในคอนโซลพร้อมสี (ข้อความปกติ)"""
        time = f"\033[32m[{datetime.now().strftime('%H:%M:%S')}]\033[0m"
        msg_log = f"{time}\033[36m:\033[0m \033[34m{msg}\033[0m"
        print(msg_log)
        
        # ใช้ Thread ในการเขียน log
        thread = threading.Thread(target=self.write_to_file, args=(msg,))
        thread.start()

    def error(self, msg):
        """ฟังก์ชันเพื่อแสดงข้อความในคอนโซลพร้อมสี (ข้อความ Error)"""
        time = f"\033[32m[{datetime.now().strftime('%H:%M:%S')}]\033[0m"
        msg_log = f"{time}\033[36m:\033[0m \033[31m{msg}\033[0m"
        print(msg_log)
        
        # ใช้ Thread ในการเขียน log
        thread = threading.Thread(target=self.write_to_file, args=(msg,))
        thread.start()

    def write_to_file(self, msg_log):
        """ฟังก์ชันสำหรับเขียน log ลงไฟล์"""
        time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        try:
            with open(self.log_file, 'a', encoding='utf-8') as file:
                file.write(f"[{time}]: {msg_log}\n")
        except Exception as e:
            print(f"Error writing to log file: {e}")


