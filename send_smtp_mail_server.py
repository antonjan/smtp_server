import smtplib, imaplib, email
import email.utils
from email.mime.text import MIMEText

import smtpd
import asyncore

class CustomSMTPServer(smtpd.SMTPServer):
    
    def process_message(self, peer, mailfrom, rcpttos, data):
        print 'Receiving message from:', peer
        print 'Message addressed from:', mailfrom
        print 'Message addressed to  :', rcpttos
        print 'Message length        :', len(data)
	b = email.message_from_string(data)
        if b.is_multipart():
                for payload in b.get_payload():
                        # if payload.is_multipart(): ...
                        print ('XXXThis is the body', payload.get_payload())
			body = payload.get_payload()
        else:
                print ('YYYYThis is the body',b.get_payload())
		body = b.get_payload()	
	smtp_host = "mail.domain"
	smtp_port = 587
	user = "user"
	passwd = "password"
	msgid = 7
	from_addr = "name@domain"
	to_addr = rcpttos 
# Create the message
# msg = MIMEText('This is the body of the message.')
	msg = MIMEText(body)
	msg['To'] = email.utils.formataddr((to_addr, to_addr))
	msg['From'] = email.utils.formataddr((from_addr, from_addr))
	msg['Subject'] = 'Giga Technology'
	print 'sending message ',body
	print 'port ', smtp_port
	print 'host server ' ,smtp_host
	print 'user ',user
	print 'reseip',rcpttos

# open authenticated SMTP connection and send message with
# specified envelope from and to addresses
	smtp = smtplib.SMTP(smtp_host, smtp_port)
	smtp.starttls()
	smtp.login(user, passwd)
	smtp.sendmail(from_addr, to_addr, msg.as_string())
	smtp.quit()

#return

server = CustomSMTPServer(('127.0.0.1', 2525), None)

asyncore.loop()

