import smtplib


smtpserver=smtplib.SMTP('smtp.gmail.com:587')
smtpserver.starttls()
passw="ynfpzyucprltscil"
smtpserver.login("ntadiko@ncsu.edu", passw)

import getpass, imaplib
import email, base64

imapserver = imaplib.IMAP4_SSL("imap.gmail.com")
imapserver.login("ntadiko@ncsu.edu", passw)
imapserver.select()
typ, data = imapserver.search(None, u'FROM "*@cybercoders.com"')
for num in data[0].split()[-1:]:
    typ, data = imapserver.fetch(num, '(RFC822)')
    
    e=email.message_from_string(data[0][1])
    #print base64.b64decode(e.get_payload())

    #print 'Message %s\n%s\n' % (num, data[0][1])
imapserver.close()
imapserver.logout()

from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.utils import COMMASPACE, formatdate

new_message = MIMEMultipart()
new_message.set_unixfrom('')
new_message['Subject'] = 'subject goes here'
#new_message['From'] = 'pymotw@example.com'
new_message['To'] = '@cybercoders.com'
new_message.set_payload('Hi I am interested. Please find my latest resume attached.\n')


print new_message
