import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

username = 'liuky008@gmail.com'
password = 'XXX'

# connect to SMTP server
# smtp_obj = smtplib.SMTP('mail.google.com', 25)

# log in
# smtp_obj.login(username, password)

# write an email
text_info = 'This a test email.'
# msg = MIMEText(text_info, 'plain', 'utf-8')

msg = MIMEMultipart('Mixed')
msg['From'] = Header(username, 'utf-8')
msg['To'] = Header('xxx@gmail.com', 'utf-8')
msg['Subject'] = Header(text_info, 'utf-8')

# send email
# smtp_obj.sendmail(msg['From'] , msg['To'], msg.as_string())

# close connection
smtp_obj.quit()


try:
    smtp_obj = smtplib.SMTP()
    smtp_obj.connect('mail.google.com', 25)
    smtp_obj.login(username, password)
    smtp_obj.sendmail(msg['From'] , msg['To'], msg.as_string())
except smtplib.SMTPException:
    print("Error: cannot send emails.")