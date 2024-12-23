from bs4 import BeautifulSoup
import smtplib
from html.parser import HTMLParser
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
    msg['From'] = f'Rose Hack <{SENDER_ACC_NAME}>'
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
            <br>
            <p> Vishra @ Citrus Hack </p>
        </body>
        </html>
        """
        send_email(email, subject, body, sender_email, sender_password)

    
    print("All Emails Sent.....")


def html_to_text(html_string):
        class HTMLTextExtractor(HTMLParser):
            def __init__(self):
                super().__init__()
                self.result = []

            def handle_data(self, data):
                self.result.append(data)

            def get_text(self):
                return ''.join(self.result)

        parser = HTMLTextExtractor()
        parser.feed(html_string)
        return parser.get_text()

def preview_email(emails, sender_email):
        subject = "Larger Demo"

        print(f'Subject: {subject}')
        body = f"""
        <html>
        <body>
            <p>Dear X,</p>
            <br>
            <p>Thank you for being a valued customer. We wanted to reach out to share some exciting updates!</p>
            <br>
            <p>Best regards,</p>
            <br>
            <p>Vishra @ Citrus Hack </p> 
        </body>
        </html>
        """
        
        print(html_to_text(body))

# Script Entry Point
if __name__ == "__main__":
    # Include file paths once you are sure who you want to send emails to
    emails = []

    sender_email = SENDER_ACC_NAME
    sender_password = APP_CRED

    q = False

    while (q != True):

        print("\n----------------------------------------")
        print("\nAutomated Email System for Hackthons")
        print("\n----------------------------------------")
        print("\n\n 1) Check Current List of Reciepients")
        print("\n\n 2) Preview Email")
        print("\n\n 3) Send Email")
        print("\n\n 4) Quit")
        print("\n----------------------------------------")

        option = int(input("\n\nPlease Select on option (1, 2, 3, 4): "))

        if option == 1:
            print("\n\n----------------------------------------")
            print("\nList of Recipients")
            print("\n----------------------------------------\n\n")

            for i in range(len(emails)):
                print(f'{i+1}) {emails[i]}')

            print("\n----------------------------------------")
            print("\n\n0) Back")
            print("\n----------------------------------------")
            option_2 = int(input("\n\nPlease Selection an Option (0): "))

            if (option_2 == 0):
                pass
            else:
                raise ValueError("Incorrect Input")
            
        elif option == 2:
            print("\n\n----------------------------------------")
            print("\nEmail Preview")
            print("\n----------------------------------------\n")
            preview_email(emails[0], sender_email)
            print("\n----------------------------------------")
            print("\n\n0) Back")
            print("\n----------------------------------------")
            option_3 = int(input("\n\nPlease Selection an Option (0): "))

            if (option_3 == 0):
                pass
            else:
                raise ValueError("Incorrect Input")
            
        elif option == 3:
            print("\n\n----------------------------------------")
            print("\nSending Preview (ALL EMAILS)")
            print("\n----------------------------------------\n")
            for i in range(len(emails)):
                print(f'{preview_email(emails[i], sender_email)}')
            print("\n----------------------------------------")
            print("\n\n1) Send Emails")
            print("\n\n2) Back")
            print("\n----------------------------------------")
            option_4 = int(input("\n\nPlease Selection an Option (1, 2): "))

            if (option_4 == 1):
                personalize_and_send_emails(emails, sender_email, sender_password)
            elif (option_4 == 2):
                pass
            else:
                raise ValueError("Incorrect Input") 
        elif option == 4:
            exit(0)
        else:
            raise ValueError("Incorrect Input")

    # # Automate sending emails
    # personalize_and_send_emails(emails, sender_email, sender_password)