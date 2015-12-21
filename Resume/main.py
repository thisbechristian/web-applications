import datetime
import logging
import os
import webapp2

from google.appengine.api import mail
from google.appengine.api import users
from google.appengine.ext.webapp import template

def render_template(handler, templatename, templatevalues={}):
	path = os.path.join(os.path.dirname(__file__), 'templates/' + templatename)
	html = template.render(path, templatevalues)
	handler.response.out.write(html)

class MainHandler(webapp2.RequestHandler):
	def get(self):
		render_template(self, 'index.html')
		
class EmailHandler(webapp2.RequestHandler):
	def get(self):
		name = self.request.get('name');
		email = self.request.get('email');
		subject = self.request.get('subject');
		message = self.request.get('message');
		comment = name +"\n"+ email +"\n"+ subject +"\n"+ message;
		admin = 'boni1331@gmail.com'
		if mail.is_email_valid(email):
			feedback = mail.EmailMessage(
				sender=admin,
				subject= subject,
				to=admin,
				body=comment
			)
			feedback.send()
			self.response.out.write('success')

mappings = [
	('/',MainHandler),
	('/email',EmailHandler)
]
app = webapp2.WSGIApplication(mappings, debug=True)