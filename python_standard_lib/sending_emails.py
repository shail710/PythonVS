from email.mime.multipart import MIMEMultipart
# above we are importing a class from email package, mime subpackage it has another subpackage multipart module
# mime stands for multi-purpose internet mail extensions
# With this object we can send email that includes both html and plain text
from pathlib import Path
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib

message = MIMEMultipart()
message['from'] = 'Shail'
message['to'] = 'shail9464@gmail.com'
message['subject'] = 'test email'
message.attach(MIMEText('Body'))
message.attach(MIMEImage(Path('img.jpg').read_bytes()))

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('shail9464@gmail.com', 'password')
    smtp.send_message(message)
    print('Sent')
