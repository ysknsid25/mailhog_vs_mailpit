import logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s:%(name)s - %(message)s",filename="logs/test.log")

def sendmail(host, port):
  import smtplib
  from email.mime.text import MIMEText
  obj_smtp= smtplib.SMTP(host, port)

  body = "メールの本文"
  msg = MIMEText(body, "html")
  msg['Subject'] = "メールの件名"
  msg['To'] = 'test@office54.net '
  msg['From'] = 'example@office54.net '

  obj_smtp.send_message(msg)
  obj_smtp.quit()

logging.info("mailhog begin")
sendmail("mailhog", 1026)
logging.info("mailhog end")
logging.info("mailpit begin")
sendmail("mailpit", 1025)
logging.info("mailpit end")