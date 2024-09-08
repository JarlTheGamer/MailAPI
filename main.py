from flask import Flask, request, jsonify
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv

# Laad omgevingsvariabelen uit een .env bestand
load_dotenv()

app = Flask(__name__)

@app.route('/send_email', methods=['POST'])
def send_email():
    data = request.json
    name = data.get('name')
    email = data.get('email')
    message = data.get('message')

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
        return jsonify({'message': 'Email sent successfully!'}), 200
    except Exception as e:
        return jsonify({'message': f'Error sending email: {e}'}), 500

if __name__ == '__main__':
    app.run(debug=False, port=3000, host="0.0.0.0")
