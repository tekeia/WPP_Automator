import schedule
import time
from datetime import datetime
from database import get_due_messages, mark_sent
import pywhatkit as pwk

def job():
    now = datetime.now()
    today = now.strftime("%Y-%m-%d")
    current_time = now.strftime("%H:%M")
    messages = get_due_messages(today, current_time)
    for msg in messages:
        msg_id, phone, date, time_str, message, sent = msg
        print(f"Enviando para {phone}: {message}")
        pwk.sendwhatmsg_instantly(phone, message, wait_time=20)
        mark_sent(msg_id)

def start_scheduler():
    schedule.every(1).minutes.do(job)
    while True:
        schedule.run_pending()
        time.sleep(1)