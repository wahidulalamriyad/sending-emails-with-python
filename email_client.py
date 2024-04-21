import smtplib
import sys
from email.message import EmailMessage
from string import Template
from pathlib import Path

first_name = sys.argv[1]
email = sys.argv[2]

html = Template(Path('index.html').read_text())
msg = EmailMessage()
msg['Subject'] = 'Welcome to the ZxN'
msg['From'] = 'Wahidul Alam Riyad'
msg['To'] = email
msg.set_content(html.substitute(name=first_name), 'html')

with smtplib.SMTP('smtp.gmail.com', 587) as server:
    server.ehlo()
    server.starttls()
    server.login('iamwarofficial@gmail.com', 'chap sequ nash szqy')
    server.send_message(msg)
    print('Email sent!')
