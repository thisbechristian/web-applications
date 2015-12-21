import time
import webapp2
import models

from google.appengine.api import mail
from google.appengine.ext import ndb

class MailHandler(webapp2.RequestHandler):
	def get(self):
		q = models.EmailConfig.query().fetch(1)
		if not q:
			config = models.EmailConfig()
			config.enabled = True
			config.put()
			mail.send_mail('boni1331@gmail.com','trjames@pitt.edu','CS1520 Sunday Evening Mail','Hello from Christian Boni :)')
		else:
			if q[0].enabled:
				mail.send_mail('boni1331@gmail.com','trjames@pitt.edu','CS1520 Sunday Evening Mail','Hello from Christian Boni :)')

class MinuteHandler(webapp2.RequestHandler):
	def get(self):	
		q = models.Thing.query().fetch(1)
		if not q:
			thing = models.Thing()
		else:
			thing = q[0]	
		thing.time = time.ctime()
		thing.put()
		
mappings = [
	('/tasks/mail',MailHandler),
	('/tasks/minute',MinuteHandler)
]
app = webapp2.WSGIApplication(mappings, debug=True)