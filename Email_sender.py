import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path
'''
can enter as many emails in the list as you want
can format the email with the usual f'{}
'''

#html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = ## Enter Email here from sender
email['to'] = ## Enter Email Address to receiver
email['subject'] = ## Enter Subject line

email.set_content ## Enter content of message

## Whatever Email Smtp protocol for email domain. and port number used.
with smtplib.SMTP(host='smtp-mail.outlook.com', port=587) as smtp:
  smtp.ehlo()
  smtp.starttls()
  smtp.login ## Enter login details for email address
  smtp.send_message(email)
  print('all good boss!')