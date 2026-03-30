import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# 🔐 Replace these with your details
SENDER_EMAIL = "nelantimeghana005@gmail.com"
APP_PASSWORD = "hjyfqwxajyfupjej"

def send_alert_email(receiver_email, similarity_score):
    subject = "⚠ TrustID Security Alert - Face Mismatch"

    body = f"""
    ALERT!

    A different face was detected during continuous verification.

    Similarity Score: {similarity_score:.4f}

    If this was not you, please check your system immediately.
    """

    msg = MIMEMultipart()
    msg["From"] = SENDER_EMAIL
    msg["To"] = receiver_email
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(SENDER_EMAIL, APP_PASSWORD)
        server.send_message(msg)
        server.quit()
        print("🚨 Alert email sent successfully!")
    except Exception as e:
        print("Email sending failed:", e)