
# Aurora Bot

Aurora Bot เป็นบอท Discord ที่มีฟังก์ชันหลากหลาย โดยสามารถใช้ในการตรวจสอบโทเค็น (Token), ดึงข้อมูลผู้ใช้, และตรวจสอบสถานะการชำระเงิน มีระบบการตั้งค่าต่างๆ ที่ช่วยให้ผู้ดูแลเซิร์ฟเวอร์สามารถใช้งานได้อย่างสะดวก

## ฟีเจอร์

- **ตรวจสอบโทเค็น (Token Check)**: ผู้ใช้สามารถตรวจสอบสถานะของโทเค็นได้
- **ข้อมูลผู้ใช้ (User Data)**: ดึงข้อมูลผู้ใช้ เช่น อีเมล และเบอร์โทรศัพท์
- **สถานะการชำระเงิน (Payment Status)**: ตรวจสอบว่าผู้ใช้มีวิธีการชำระเงินตั้งไว้หรือไม่
- **ปรับแต่งโปรไฟล์บอท (Customizable Profile)**: บอทสามารถปรับแต่งชื่อและภาพโปรไฟล์ได้ในตอนเริ่มต้น

## ข้อกำหนด

ก่อนที่คุณจะรัน Aurora Bot คุณต้องติดตั้งสิ่งเหล่านี้:

1. **Python 3.8+**
   - คุณสามารถดาวน์โหลด Python ได้จากเว็บไซต์ทางการ: https://www.python.org/downloads/

2. **pip** (Python package installer)
   - ใช้สำหรับติดตั้ง dependencies ที่จำเป็น โดยปกติจะติดตั้งมาพร้อมกับ Python 3.8+

3. **Dependencies**
   - ติดตั้ง dependencies ทั้งหมดโดยใช้คำสั่ง:
   ```bash
   pip install -r requirements.txt

4. Discord Bot Token

คุณต้องมี Discord Bot Token เพื่อรันบอท หากคุณยังไม่ได้สร้างบอท สามารถดูวิธีการสร้างบอทและรับโทเค็นได้ที่ คู่มือการสร้างบอท Discord



5. ไฟล์ Config (config.json)

บอทใช้ไฟล์ config.json สำหรับการตั้งค่าต่างๆ อย่าลืมสร้างไฟล์นี้ในรูปแบบต่อไปนี้:




{
  "TOKEN": "YOUR_BOT_TOKEN",
  "LOG": "path/to/log/file.log",
  "BOT": {
    "name": "Aurora",
    "profile": "https://example.com/profile_image.jpg"
  }
}

แทนที่ YOUR_BOT_TOKEN ด้วยโทเค็นของคุณเอง

ฟิลด์ LOG คือลิงก์ของไฟล์บันทึกที่บอทจะใช้สำหรับบันทึกกิจกรรม

ฟิลด์ BOT ใช้สำหรับตั้งชื่อและ URL ของภาพโปรไฟล์บอท


การติดตั้ง

ขั้นตอนที่ 1: โคลนรีโพซิทอรี

โคลนรีโพซิทอรีนี้ไปยังเครื่องของคุณ:

git clone https://github.com/yourusername/aurora-bot.git
cd aurora-bot

ขั้นตอนที่ 2: ติดตั้ง dependencies

ติดตั้ง dependencies ทั้งหมด:

pip install -r requirements.txt

ขั้นตอนที่ 3: สร้างไฟล์ config.json

สร้างไฟล์ config.json ในโฟลเดอร์หลักของโปรเจกต์ (ในที่เดียวกับ README.md) โดยใช้รูปแบบที่กล่าวถึงข้างต้น

ขั้นตอนที่ 4: รันบอท

หลังจากติดตั้งเสร็จสิ้น คุณสามารถรันบอทด้วยคำสั่ง:

python bot.py

หลังจากรันบอทเสร็จ คุณจะเห็นข้อความในเทอร์มินัลที่บอกว่า:

Login as <Bot Name>

การใช้งาน

เมื่อบอทเริ่มทำงานแล้ว คุณสามารถใช้คำสั่งดังต่อไปนี้:

/setup: ตั้งค่าบอทและแสดงเมนูที่มีตัวเลือกต่างๆ

เช็คโทเค็น (Token Check): ผู้ใช้สามารถคลิกที่ปุ่ม เช็ค Token เพื่อเปิด Modal สำหรับกรอกโทเค็น


คำสั่ง

/setup

ตั้งค่าบอทและส่งข้อความแนะนำกับตัวเลือกให้ผู้ใช้

การคลิกปุ่ม:

เช็ค Token: เปิด Modal สำหรับกรอกโทเค็นของผู้ใช้เพื่อตรวจสอบ


การบันทึก (Logging)

บอทใช้ระบบการบันทึกกิจกรรม (Log) โดยข้อมูลทั้งหมดจะถูกบันทึกลงในไฟล์ที่ระบุใน config.json ในฟิลด์ LOG

ตัวอย่างบันทึก:

Bot is in 1 guilds
Guild Name: Example Server, Guild ID: 123456789012345678
Login as Aurora Bot
Received token input for verification.
Successfully retrieved data for user: username#1234
User token: MTA2MDExNzI5NjQzOTg0NjMwOA.XXXXXX.XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
User email: example@example.com
User phone: 123-456-7890
Payment method status: พบวิธีการชำระเงิน ✅
Embed successfully created, sending to user.
Embed sent successfully.

การมีส่วนร่วม

หากคุณต้องการมีส่วนร่วมในการพัฒนา Aurora Bot สามารถทำการ Fork โค้ดมาแล้วสร้าง Branch ใหม่ จากนั้นทำการส่ง Pull Request เพื่อขอรวมการเปลี่ยนแปลง

ใบอนุญาต

โปรเจกต์นี้ใช้ใบอนุญาต MIT License - ดูรายละเอียดเพิ่มเติมได้ที่ไฟล์ LICENSE


---

พัฒนาโดย NSTIOM Inc. | Powered by Aurora X
