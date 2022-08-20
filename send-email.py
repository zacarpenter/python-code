# Send an email from a Gmail account
import smtplib
import ssl
from email.message import EmailMessage

subject = "Email from Python"
body = "This is a test email from Python!"
sender_email = "zcarpenter.smtp.tester@gmail.com"
reciever_email = "carpenterzac0810@gmail.com"
password = input("Enter the account password: ")