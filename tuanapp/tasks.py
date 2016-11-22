import smtplib, email, time
from celery import task
from email.mime.text import MIMEText

from tuanapp.models import Tuan, Person, Comment

def SendEmail(Sender, Receiver, Subject, Text):
    msg = MIMEText(Text, 'html')
  msg['Subject'] = Subject
  msg["To"] = ";".join(Receiver)
  msg["From"] = Sender
  smtp = smtplib.SMTP('localhost')
  smtp.sendmail(Sender, Receiver, msg.as_string())
  smtp.quit()

@task()
def CheckTime():
    for t in Tuan.objects.all():
        try:
            TarTime = time.mktime(time.strptime(str(t.date), '%Y-%m-%d %H:%M'))
    except:
        continue

    #if abs(TarTime - time.time()) / 60 - 15 >= 0.5:
    if abs(TarTime - time.time()) / 60 - 15 <= 2.5:
        Sender = 'xuym@synopsys.com'
      Receiver = []
      Subject = '[Fan Tuan] Your Tuan on %s at %s is approaching' % (t.date, t.rest_name)
      Text = '''
      Please join!
      Have nice time~
      '''
      for p in t.joind_id.all():
          Receiver.append(str(p.email))

      if Receiver:
          SendEmail(Sender, Receiver, Subject, Text)
      print Sender, Receiver, Subject, Text
  else:
      return 5

