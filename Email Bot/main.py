import smtplib
import schedule
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

def send_email(sender_email, sender_password, receiver_email, subject, content):
    try:
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = subject
        msg.attach(MIMEText(content, 'plain'))

        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.send_message(msg)

        print(f"✅ Email sent to {receiver_email} successfully.")
    except Exception as e:
        print(f"❌ Failed to send email. Reason: {e}")

def schedule_email(send_time, func, *args):
    def job():
        current_time = datetime.now().strftime('%H:%M')
        if current_time == send_time:
            func(*args)
            return schedule.CancelJob
    schedule.every(1).minutes.do(job)

def main():
    print("🔐 Enter sender's Gmail credentials:")
    sender_email = input("Sender Email: ")
    sender_password = input("Sender App Password: ")

    receiver_email = input("Receiver Email: ")
    subject = input("Email Subject: ")
    content = input("Email Content: ")
    send_time = input("Schedule Time (HH:MM in 24hr format): ")

    print("⏳ Scheduling email...")
    schedule_email(send_time, send_email, sender_email, sender_password, receiver_email, subject, content)

    while True:
        schedule.run_pending()
        time.sleep(30)

if __name__ == "__main__":
    main()
