import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path


html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = ''
email['to'] = ''
email['subject'] = 'Subject'

email.set_content(html.substitute({'name': 'Joe Bloggs'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('amend', 'amend')
    smtp.send_message(email)
    print('email sent')
    
