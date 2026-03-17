# BulkEmail

BulkEmails is a lightweight Python script that sends the same email to multiple recipients, one by one, using Gmail’s SMTP server. It reads recipient email addresses from a text file and can optionally attach a file (currently configured for PDFs).

---

## Features

- Sends emails individually to each recipient (no visible mailing list).
- Uses Gmail SMTP with TLS for secure delivery.
- Supports attaching a file to each email (default setup is for PDF).
- Reads recipients from a `.txt` file (one email address per line).
- Adds a short delay between emails to reduce spam-like behavior.
- Prints progress and status messages in the terminal.

---

## Requirements

- Python 3.x installed.
- A Gmail account.
- A Gmail **App Password** (not your normal Gmail password).
- Internet connection to reach Gmail’s SMTP server.

> You can create an App Password from your Google Account → Security → App passwords.

---

## Installation

1. Clone this repository or download the project folder:

   ```bash
   git clone https://github.com/your-username/BulkEmails.git
   cd BulkEmails
2.	(Optional but recommended) Create and activate a virtual environment:
bash
python -m venv venv
# On macOS/Linux
source venv/bin/activate
# On Windows
venv\Scripts\activate
3.	No extra packages are required because the script uses only Python’s standard library.
________________________________________
Configuration
Open BulkEmails.py and edit the configuration section at the top:
python
SMTP_SERVER = "smtp.gmail.com"

SMTP_PORT = 587

SENDER_EMAIL = "YourEmail@gmail.com"

SENDER_PASSWORD = "abcd efgh ijkl mnop"  # Gmail App Password

SUBJECT = "Title of the email"

BODY = """
Body of the email
"""

ATTACHMENT_PATH = "Attachment.pdf"  # File you want to attach

RECIPIENTS_FILE = "Example.txt"     # Text file with one email per line

Explanation of the main settings:

•	SENDER_EMAIL: Your Gmail address that will send the emails.

•	SENDER_PASSWORD: The Gmail App Password (do not share this with anyone).

•	SUBJECT: Subject line of your email.

•	BODY: The body text of the email.

•	ATTACHMENT_PATH: Path to the file to attach. If the file does not exist, the script shows a warning and sends the email without an attachment.

•	RECIPIENTS_FILE: Path to a text file that contains the recipient email addresses, one per line.

Example Example.txt:

text

user1@example.com

user2@example.com

user3@example.com
________________________________________
Usage
1.	Set SENDER_EMAIL and SENDER_PASSWORD in BulkEmails.py.
   
2.	Edit SUBJECT and BODY with the email content you want to send.
   
3.	Prepare your recipients file (e.g., Example.txt) with one email per line.

4.	Place your attachment file in the project folder and set ATTACHMENT_PATH to its name (or full path).

5.	Run the script:
   
bash

python BulkEmails.py

What happens when you run it:


•	The script loads all recipients from RECIPIENTS_FILE.

•	It connects to Gmail’s SMTP server using TLS and logs in with your sender account.

•	It sends the email (and attachment, if present) to each recipient individually.

•	It prints progress messages like Sending... 1/10 To user@example.com....

•	It waits a short time between each email and prints a final success or error message.

________________________________________
Attachments

By default, the script is configured to attach a PDF file (e.g., Attachment.pdf). If the attachment file is missing, the script warns you and sends the emails without any attachment.

You can point ATTACHMENT_PATH to any file you want, but for full compatibility with different file types you may need to adjust the code to set the correct MIME type.
________________________________________
Security Notes
•	Do not commit your real SENDER_EMAIL or SENDER_PASSWORD to a public repository.

•	Treat the App Password like a real password: never share it, and revoke it if you suspect it has been exposed.

•	For production use, consider loading credentials from environment variables or a separate, ignored config file instead of hard-coding them.

________________________________________
Example Use Cases
•	Sending announcements or newsletters to a small mailing list.

•	Emailing all students in a class.

•	Notifying colleagues or clients with a standard message and attachment.

