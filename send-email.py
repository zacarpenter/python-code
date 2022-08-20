from email import message
import smtplib
import ssl
from email.message import EmailMessage

subject = "Email from Python"
body = "This is a test email from Python!"
# Sender email not working - can't enable less secure settings in Yahoo/Gmail
sender_email = "zcarpenter.smtp.tester@yahoo.com"
reciever_email = "carpenterzac0810@gmail.com"
password = input("Enter the account password: ")

message = EmailMessage()
message["From"] = sender_email
message["To"] = reciever_email
message["Subject"] = subject
message.set_content(body)

context = ssl.create_default_context()

print("Sending Email")
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, reciever_email, message.as_string())

print("Success!")