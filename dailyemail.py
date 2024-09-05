#pip install schedule

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
    password = "31557225009"