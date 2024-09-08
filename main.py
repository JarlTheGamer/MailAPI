import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv

# Laad omgevingsvariabelen uit een .env bestand
load_dotenv()

def send_email(name, email, message):
    # Configure SMTP server
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    smtp_user = os.getenv('EMAIL_USER')  # Je email uit omgevingsvariabelen
    smtp_password = os.getenv('EMAIL_PASS')  # Je wachtwoord uit omgevingsvariabelen

    # Maak een emailbericht
    msg = MIMEMultipart()
    msg['From'] = email
    msg['To'] = 'your-work-email@example.com'  # Je privé werk email
    msg['Subject'] = f'Form submission from {name}'

    body = f'Name: {name}\nEmail: {email}\nMessage: {message}'
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Verbind met de SMTP-server en stuur de e-mail
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_user, smtp_password)
            server.send_message(msg)
        print('Email sent successfully!')
    except Exception as e:
        print(f'Error sending email: {e}')

# Voorbeeldgebruik
if __name__ == '__main__':
    send_email('John Doe', 'john.doe@example.com', 'Hello, this is a test message.')
