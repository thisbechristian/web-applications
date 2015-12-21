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

mappings = [
	('/',MainHandler),
]
app = webapp2.WSGIApplication(mappings, debug=True)