#pip install schedule

from cmath import e
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import schedule
import time
from datetime import datetime

# Function to send email
def send_email():
    # Email configuration
    sender_email = "willfrazier715@gmail.com"
    receiver_email = "trevormwangi94@gmail.com"
    password = "EternalAtakeno.1!"

    # Create the email header
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = (f"Daily Report - {datetime.now().strftime('%Y-%m-%d')}")

    body = 'This is the daily report'
    msg.attach(MIMEText(body, 'plain'))



    # Send the email
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, password)
        text = msg.as_string()
        server.sendmail(sender_email, receiver_email, text)
        server.quit()
        print(f'Email sent to {receiver_email} on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}')
    except Exception as e:
        print(f'Failed to send email. Error: {str(e)}')

# Schedule the email to be sent daily
schedule.every().day.at('08:00').do(send_email)  # Set the time you want to send the email

if __name__ == '__main__':
    while True:
        schedule.run_pending()
        time.sleep(1)