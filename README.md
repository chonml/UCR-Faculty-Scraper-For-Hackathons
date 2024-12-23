# Web Scraper for UCR Hackathon Contacts

I created this webscraper/email messenger to expedite the emailing process of reaching out to UCR personel for Hackathons. I will continue building this to adjust for email signatures and email blacklisting for those who don't want to be emailed.

# Hackathons Used In
1. Cutie Hack 2024
2. Citrus Hack 2025
3. Rose Hack 2025

# Instructions
## Installing Proper Python Version and Libraries
1. Install Python (I'm using 3.9.12)
2. Please run:
`pip install bs4 smtplib html.parser email.mime.text email.mime.multipart email.mime.image python_dotenv os`

## Setting up app password for email automation

In order to use email automation with your email you will need to create a app password with google. Please go to https://myaccount.google.com/ and follow the navigation below:

Security > App Passwords > Create New App Password for GMAIL

Once you created your app passkey immediately create a .env in the home directory and fill in the following variables:

![ENV_PICTURE][env_pic.png]