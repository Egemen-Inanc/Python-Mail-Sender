from email.message import EmailMessage
import ssl
import smtplib
print("""
 _____ _____  ________  ___  ___  _____ _
|  ___|  __ \|  ___|  \/  | / _ \|_   _| |
| |__ | |  \/| |__ | .  . |/ /_\ \ | | | |
|  __|| | __ |  __|| |\/| ||  _  | | | | |
| |___| |_\ \| |___| |  | || | | |_| |_| |____
\____/ \____/\____/\_|  |_/\_| |_/\___/\_____/

                                              
""")
email_sender = input("Enter your email address:")
email_password = input("Your application password:")
email_reciever = input("Enter the email receiver:")
subject = input("subject:")
content = input("""your message:""")
em = EmailMessage()
em['From']=email_sender
em['To']=email_reciever
em['subject'] =subject
em.set_content(content)
context = ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com',465, context=context) as smtp:
    smtp.login(email_sender,email_password)
    smtp.sendmail(email_sender,email_reciever,em.as_string())
