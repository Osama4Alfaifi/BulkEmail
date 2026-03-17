import smtplib
from email.message import EmailMessage
from pathlib import Path
import time

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

SENDER_EMAIL = "YourEmail@gmail.com"
SENDER_PASSWORD = "abcd efgh ijkl mnop" # The password should look like this. DONT SHARE IT WITH ANYONE
#go to link below to create the password require in SENDER_PASSWORD variable
#https://myaccount.google.com/apppasswords?continue=https://myaccount.google.com/security?gar%3DWzEyMF0%26hl%3Den%26utm_source%3DOGB%26utm_medium%3Dact&pli=1&rapt=AEjHL4P7pvhfuPlOWxY9MavRjktroUq04BL43QJBEgZ7tRxcZkuQxW2kcU_T8MqF7FaRkPfW7Ci0U0I-4FZNYQEY2lJDEGK-5VK7XIDh10NPzwLmiRWt1Cs
SUBJECT = "Title of the email"

BODY = """
Body of the email
"""

ATTACHMENT_PATH = "Attachment.pdf" # File you want to attach to the email
RECIPIENTS_FILE = "Example.txt"  # the text file that contains an email in each line

def load_recipients(path: str):
    with open(path, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]

def build_message(sender: str, recipient: str) -> EmailMessage:
    msg = EmailMessage()
    msg["From"] = sender
    msg["To"] = recipient
    msg["Subject"] = SUBJECT
    msg.set_content(BODY)

    file_path = Path(ATTACHMENT_PATH)
    if file_path.exists():
        with open(file_path, "rb") as f:
            data = f.read()
        msg.add_attachment(
            data,
            maintype="application",
            subtype="pdf",
            filename=file_path.name,
        )
    else:
        print(f"WARNING {ATTACHMENT_PATH} DOESN'T EXIST")

    return msg

def main():
    recipients = load_recipients(RECIPIENTS_FILE)
    print(f"Email will be sent individually to {len(recipients)}...")

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            
            for i, recipient in enumerate(recipients, 1):
                print(f"Sending...  {i}/{len(recipients)} To {recipient}...")
                msg = build_message(SENDER_EMAIL, recipient)
                server.send_message(msg)
                print(f"✅ Sent to {recipient}")
                
                # 2 seconds delay between emails
                if i < len(recipients):
                    time.sleep(2)
                    
        print("🎉 Emails sent successfully")
    except Exception as e:
        print(f"❌ Error in sending email {e}")

if __name__ == "__main__":
    main()
