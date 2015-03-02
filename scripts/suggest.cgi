#!/usr/bin/env python
import cgi
import re
import smtplib
from email.mime.text import MIMEText

form = cgi.FieldStorage()
try:
  video_id = re.search(r'v=([^&]+)', form.getfirst('url')).group(1)
except:
  video_id = "unknown"

# Define email contents here:
FROM = ''
TO = []
SUBJECT = ''
BODY = ''

msg = MIMEText(BODY)
msg['Subject'] = SUBJECT
msg['To'] = reduce(lambda x,y: '%s,%s' % (x,y), TO) # *drool*
msg['From'] = FROM
server = smtplib.SMTP('localhost')
server.sendmail(FROM, TO, msg.as_string())
server.quit()

print "Location: http://www.artworksinmotion.com/thankyou/\n\n"
