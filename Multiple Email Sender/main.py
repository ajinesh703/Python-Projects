# Multiple Account Email Sender
# Requires: less secure app access (or app password) enabled for each Gmail account

import smtplib
from email.mime.text import MIMEText

# List of sender accounts (email, app_password)
accounts = [
    ("your_email_1@gmail.com", "app_password_1"),
    ("your_email_2@gmail.com", "app_password_2")
]

# List of recipients
recipients = ["receiver1@example.com", "receiver2@example.com"]

subject = "Test Email from Python"
body = "This is a test email sent using multiple accounts."

def send_email(sender_email, password, to_list, subject, body):
    try:
        msg = MIMEText(body)
        msg["Subject"] = subject
        msg["From"] = sender_email
        msg["To"] = ", ".join(to_list)

        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.login(sender_email, password)
        server.sendmail(sender_email, to_list, msg.as_string())
        server.quit()

        print(f"Email sent from {sender_email} ✅")
    except Exception as e:
        print(f"Failed from {sender_email}: {e}")

if __name__ == "__main__":
    for email, pwd in accounts:
        send_email(email, pwd, recipients, subject, body)
