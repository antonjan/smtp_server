import smtplib
import email.utils
from email.mime.text import MIMEText
from email.header import Header

to = 'test@test.com'
# Create the message
msg = MIMEText('This is the body of the message.3 ')
#msg['To'] =  'anton.janovsky@gmail.com'
msg['To'] = Header(to, 'utf-8')
msg['From'] = email.utils.formataddr(('test@test.com', 'test@test'))
msg['Subject'] = 'subject is Simple test message 3'

server = smtplib.SMTP('127.0.0.1', 2526)
server.set_debuglevel(True) # show communication with the server
try:
#	server.connect()
    	server.sendmail('test@test.co.za', ['test@test.com'], msg.as_string())
finally:
    	server.quit()
