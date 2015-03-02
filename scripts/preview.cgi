#!/usr/bin/env python
import cgi
from artworksinmotion import ENV

form = cgi.FieldStorage()
id = form.getfirst('id')
template = ENV.get_template('preview.html')
html = template.render(id=id)
print 'Content-Type: text/html\n\n'
print html
