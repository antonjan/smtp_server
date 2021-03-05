import smtplib
import email.utils
from email.mime.text import MIMEText
from email.header import Header

to = 'anton.janovsky@gmail.com'
# Create the message
msg = MIMEText('This is the body of the message.3 ')
#msg['To'] =  'anton.janovsky@gmail.com'
msg['To'] = Header(to, 'utf-8')
msg['From'] = email.utils.formataddr(('shop@giga.co.za', 'shop@giga.co.za'))
msg['Subject'] = 'subject is Simple test message 3'

server = smtplib.SMTP('127.0.0.1', 2526)
server.set_debuglevel(True) # show communication with the server
try:
#	server.connect()
    	server.sendmail('shop@giga.co.za', ['anton.janovsky@gmail.com'], msg.as_string())
finally:
    	server.quit()
