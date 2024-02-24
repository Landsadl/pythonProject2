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
email['from'] = 'benchwarmer_5@hotmail.com'
email['to'] = 'adavisla@uark.edu'
email['subject'] = 'Possible Job Offer'

email.set_content(' I was reaching out to you in regards to a possible job opportunity hit me up please' )

with smtplib.SMTP(host='smtp-mail.outlook.com', port=587) as smtp:
  smtp.ehlo()
  smtp.starttls()
  smtp.login('benchwarmer_5@hotmail.com', 'KAPPa353!')
  smtp.send_message(email)
  print('all good boss!')