import datetime
import logging
import os
import webapp2
import models

from google.appengine.api import mail
from google.appengine.api import users
from google.appengine.ext import ndb
from google.appengine.ext.webapp import template

def render_template(handler, templatename, templatevalues={}):
	path = os.path.join(os.path.dirname(__file__), 'templates/' + templatename)
	html = template.render(path, templatevalues)
	handler.response.out.write(html)

class MainHandler(webapp2.RequestHandler):
	def get(self):
		params = {}
		
		q = models.Thing.query().fetch(1)
		if q:
			thing = q[0]
			params['time'] = thing.time
			
		q = models.EmailConfig.query().fetch(1)
		if not q:
			config = models.EmailConfig()
			config.enabled = True
			config.put()
		else:
			config = q[0]
			
		if config.enabled:
			params['config'] = 'ON'
		else:
			params['config'] = 'OFF'
			
		render_template(self, 'index.html', params)
		
class ConfigHandler(webapp2.RequestHandler):
	def post(self):
		q = models.EmailConfig.query().fetch(1)
		config = q[0]
		config.enabled = not config.enabled
		config.put()
		setting = "ON" if config.enabled else "OFF"
		config_JSON = '{"config": "' + setting + '"}'
		self.response.out.write(config_JSON)
		

mappings = [
	('/',MainHandler),
	('/config',ConfigHandler)
]
app = webapp2.WSGIApplication(mappings, debug=True)