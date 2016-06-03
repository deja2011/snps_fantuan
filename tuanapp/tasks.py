import smtplib, email
from celery import task
from email.mime.text import MIMEText

def SendEmail(sender, receiver, subject, text):
  msg = MIMEText(text, 'html')
  msg['Subject'] = subject
  msg["To"] = ";".join(receiver)
  msg["From"] = sender
  smtp = smtplib.SMTP('localhost')
  smtp.sendmail(sender, receiver, msg.as_string())
  smtp.quit()

@task()
def CheckTime():
  if 1:
    sender, receiver, subject, text = 'xuym@synopsys.com', ['xuym@synopsys.com',], 'Test', 'Test1'
    SendEmail(sender, receiver, subject, text)
    return 1
  else:
    return 5

