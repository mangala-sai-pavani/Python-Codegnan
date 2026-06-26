#try with 3.12 version

import smtplib
from email.message import EmailMessage

sender_mail = "saipavani175@gmail.com"
password = "kbbmlmzawldzbexl"

reciever_email = "sownyakoribilli@gmail.com"

msg = EmailMessage()
msg['Subject'] = "Python Email Authentication"
msg['From'] = sender_mail
msg['To'] = reciever_email

msg.set_content("Hello Student,\nThis email is sent using python.")

server = smtplib.SMTP_SSL('smtp.gmail.com',465)
server.starttls()
server.login(sender_mail,password)

server.send_message(msg)

server.quit()

print("Email sent Successfully.")
