from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText

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
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = 'Rose Hack <rosehackucr@gmail.com>'
    msg['To'] = to_email
    
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

        # Create a personalized email body
        body = f""
        subject = f""

        print(body, subject)
        send_email(email, subject, body, sender_email, sender_password)

# Script Entry Point
if __name__ == "__main__":
    emails = [
        "Insert Emails Here"
    ]

    valid_emails = []
    
    print("Extracted Emails:")

    for email in emails: valid_emails.append(email)
    
    # Sender credentials
    sender_email = "" 
    sender_password = "" 

    # Automate sending emails
    personalize_and_send_emails(valid_emails, sender_email, sender_password)