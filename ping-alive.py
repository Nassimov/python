import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# List of servers to monitor
SERVERS = ["8.8.8.8","nonexistent.example.com"]

# Outlook SMTP Configuration
SMTP_SERVER = "smtp.office365.com"
SMTP_PORT = 587
EMAIL_SENDER = "nacimessi10@outlook.fr"
EMAIL_PASSWORD = "Motdepasse1010*"  # Use the generated App Password
EMAIL_RECEIVER = "nacimessi10@outlook.fr"

def ping_server(server):
    """Ping a server and return True if it's up, False if it's down."""
    response = os.system(f"ping -c 1 {server} > /dev/null 2>&1")
    return response == 0  # 0 means success, other values mean failure

def send_email_alert(down_servers):
    """Send an email notification if any server is down."""
    subject = "🚨 Server Down Alert!"
    body = f"The following servers are not responding:\n\n" + "\n".join(down_servers)

    msg = MIMEMultipart()
    msg["From"] = EMAIL_SENDER
    msg["To"] = EMAIL_RECEIVER
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL_SENDER, EMAIL_PASSWORD)
        server.sendmail(EMAIL_SENDER, EMAIL_RECEIVER, msg.as_string())
        server.quit()
        print("📧 Email alert sent successfully!")
    except Exception as e:
        print(f"⚠️ Failed to send email: {e}")

def check_servers():
    """Check all servers and send an alert if any are down."""
    down_servers = [server for server in SERVERS if not ping_server(server)]

    if down_servers:
        print(f"🚨 Alert! The following servers are down: {down_servers}")
        send_email_alert(down_servers)
    else:
        print("✅ All servers are up.")

# Run the server check
if __name__ == "__main__":
    check_servers()
