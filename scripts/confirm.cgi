#!/usr/bin/env python
import cgi
import cgitb
cgitb.enable()
from artworksinmotion import VIDEOS, addvideo, populate, write_db

form = cgi.FieldStorage()
video = {}
video['slug']  = form.getvalue('slug')
video['title'] = form.getvalue('title')
video['descr'] = form.getvalue('description')
video['yt_id'] = form.getvalue('id')

addvideo(video['yt_id'])
VIDEOS.append(video)
populate()
write_db()

print "Location: http://www.artworksinmotion.com/%s/\n\n" % video["slug"]
