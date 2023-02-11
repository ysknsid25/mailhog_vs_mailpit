import logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s:%(name)s - %(message)s",filename="logs/test.log")

def sendmail(host, port):
  import smtplib
  from email.mime.text import MIMEText
  from email.mime.multipart import MIMEMultipart
  from email.mime.application import MIMEApplication
  smtp_obj = smtplib.SMTP(host, port)
  # mailpitのみSMTPS, SMTP_AUTHのどちらも設定している
  # smtp_obj.starttls()
  # smtp_obj.login('user', 'pass')

  body = "メールの本文"
  msg = MIMEMultipart()
  msg['Subject'] = "メールの件名"
  msg['To'] = 'to@office54.net'
  msg['From'] = 'from@office54.net '
  msg.attach(MIMEText(body))

  with open(r"/src/img/1MB.jpeg", "rb") as f:
      attachment = MIMEApplication(f.read())

  attachment.add_header("Content-Disposition", "attachment", filename="1MB.jpeg")
  msg.attach(attachment)
  smtp_obj.send_message(msg)
  smtp_obj.quit()

logging.info("mailhog begin")
sendmail("mailhog", 1026)
logging.info("mailhog end")
logging.info("mailpit begin")
sendmail("mailpit", 1025)
logging.info("mailpit end")