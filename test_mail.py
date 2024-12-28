import smtplib , ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

sender="andy87228@gmail.com"
receiver=["andy87228@icloud.com","andy-cheng@shinymark.com"]
passwd="snfb oiim wlon tycy"
for i in receiver:
    msg = MIMEMultipart()
    msg["From"] = sender
    msg["To"] = i
    msg["Subject"]=Header("Test send email","utf-8").encode()

    body="This is send by python\nhello world"

    msg_text=MIMEText(body)
    msg.attach(msg_text)
    c=ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com",465,context=c) as sever:
        sever.login(sender,passwd)
        sever.sendmail(sender,i,msg.as_string())
    print("Success send email to {}".format(i))