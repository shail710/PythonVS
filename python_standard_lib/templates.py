from email.mime.multipart import MIMEMultipart
# above we are importing a class from email package, mime subpackage it has another subpackage multipart module
# mime stands for multi-purpose internet mail extensions
# With this object we can send email that includes both html and plain text
from pathlib import Path
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from string import Template
import smtplib

template = Template(Path('template.html').read_text())
body = template.substitute({'name': 'Shail'})
message = MIMEMultipart()
message['from'] = 'Shail'
message['to'] = 'shail9464@gmail.com'
message['subject'] = 'test email'
message.attach(MIMEText(body, 'html'))
message.attach(MIMEImage(Path('img.jpg').read_bytes()))

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('shail9464@gmail.com', 'password')
    smtp.send_message(message)
    print('Sent')
