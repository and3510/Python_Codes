import os
import smtplib
from email.message import EmailMessage
from segredos import senha

EMAIL_ADDRESS = "alisonleao.01@gmail.com"
EMAIL_PASSWORD = senha

msg = EmailMessage()
msg['Subject'] = 'ola meu é #$#%#$'
msg['from'] = "alisonleao.01@gmail.com"
msg['To'] = "and.dovale@gmail.com"
msg.set_content("Testando meu amigo")

with smtplib.SMTP_SLL('smtp.gmail.com',465) as smtp:
    smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
    smtp.send_message(msg)
