from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from dotenv import load_dotenv
import os

load_dotenv()

# Loading in credentials
APP_CRED = os.getenv('APP_CRED')
SENDER_ACC_NAME = os.getenv('SENDER_ACC_NAME')
SIGNATURE_PATH = os.getenv('SIGNATURE_PATH')

# Website to Scrape
file_path = "UCR Profiles - Search & Browse.html"

# UCR Personnel Email Scraper
def extract_emails_from_html(file_path):
    # Read the file content
    with open(file_path, "r", encoding='latin-1') as file:
        html_content = file.read()
    
    # Parse the HTML
    soup = BeautifulSoup(html_content, "html.parser")
    
    # Find all <a> tags with 'mailto:' in their href attribute
    email_tags = soup.find_all("a", href=lambda href: href and href.startswith("mailto:"))
    
    # Extract and clean email addresses
    emails = {tag['href'].replace("mailto:", "").strip() for tag in email_tags}
    
    return sorted(emails)

# Sends email
def send_email(to_email, subject, body, sender_email, sender_password):
    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = f'Go stupid go crazy ahhh <{SENDER_ACC_NAME}>'
    msg['To'] = to_email

    msg.attach(MIMEText(body, 'html'))

    with open(SIGNATURE_PATH, "rb") as img_file:  # Replace with your signature image path
        img = MIMEImage(img_file.read())
        img.add_header('Content-ID', SIGNATURE_PATH)
        img.add_header('Content-Disposition', 'inline', filename=SIGNATURE_PATH)
        msg.attach(img)
    
    try:
        # Connect to the SMTP server
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()  
            server.login(sender_email, sender_password)  # Login to the sender's email account
            server.send_message(msg)
            
        print(f"Email sent to {to_email}")

    except Exception as e:
        print(f"Failed to send email to {to_email}: {e}")

#Insert other logic here to format emails to personalize emails
def personalize_and_send_emails(emails, sender_email, sender_password):
    for email in emails:
        subject = "Larger Demo"
        body = f"""
        <html>
        <body>
            <p>Dear X,</p>
            <br>
            <p>Thank you for being a valued customer. We wanted to reach out to share some exciting updates!</p>
            <br>
            <p>Best regards,</p>
            <p><b>Your Company</b></p>
            <img src="cid:{SIGNATURE_PATH}" alt="Signature Image" style="width:200px;height:auto;">
        </body>
        </html>
        """

        print(body, subject)
        send_email(emails, subject, body, sender_email, sender_password)

# Script Entry Point
if __name__ == "__main__":
    emails = ["jdari003@ucr.edu", "jonathan.darius2015@gmail.com"]
    
    # Sender credentials
    sender_email = SENDER_ACC_NAME
    sender_password = APP_CRED

    # Automate sending emails
    personalize_and_send_emails(emails, sender_email, sender_password)