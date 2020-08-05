import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path


''' use simonhowlett.dev@gmail.com '''

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Simon Howlett'
email['to'] = 'simonjhowlett@gmail.com'
email['subject'] = 'Testing Python Script'

email.set_content(html.substitute({'name': 'Simon'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('amend', 'amend')
    smtp.send_message(email)
    print('email sent')
