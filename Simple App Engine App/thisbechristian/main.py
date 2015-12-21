import datetime
import logging
import os
import webapp2

from google.appengine.ext.webapp import template
from google.appengine.api import users
from google.appengine.ext import ndb
from google.appengine.api import images
from google.appengine.ext import blobstore
from google.appengine.ext.webapp import blobstore_handlers

def template_to_html(handler, template_name, template_values={}):
	path = os.path.join(os.path.dirname(__file__), 'templates/' + template_name)
	html = template.render(path, template_values)
	handler.response.out.write(html)
	
def get_email():
	result = None
	user = users.get_current_user()
	if user:
		result = user.email()
	return result
	
def get_member(email):
	if email:
		return Member.get_by_id(email)
	return None
	
class Member(ndb.Model):
	name = ndb.StringProperty()
	notes = ndb.TextProperty()
	date = ndb.DateTimeProperty()

class MainHandler(webapp2.RequestHandler):
    def get(self):
    	email = get_email()
    	member = get_member(email)
    	user_name = None
    	user_notes = None
    	user_date = None

    	if member:
    		user_name = member.name
    		user_notes = member.notes
    		user_date = member.date
    	
    	params = {
    		'user_email': email,
    		'login_url': users.create_login_url(),
    		'logout_url': users.create_logout_url('/'),
    		'user_name': user_name,
    		'user_notes': user_notes,
    		'user_date': user_date
    	}
    	template_to_html(self, "index.html", params)
    
class EditUser(webapp2.RequestHandler):
	def get(self):
		email = get_email()
		if email:
			member = get_member(email)
			user_name = None
			user_notes = None
			user_date = None

			if member:
				user_name = member.name
				user_notes = member.notes
				user_date = member.date
		
			params = {
				'user_email': email,
				'login_url': users.create_login_url(),
				'logout_url': users.create_logout_url('/'),
				'user_name': user_name,
				'user_notes': user_notes,
				'user_date': user_date
			}
			template_to_html(self, "edit.html", params)
		else:
			self.redirect('/')
		
class CommitUser(webapp2.RequestHandler):
	def post(self):
		email = get_email()
		if email:
			member = Member.get_or_insert(email)
			member.name = self.request.get('name')
			member.notes = self.request.get('notes')
			member.date = datetime.datetime.now()
			member.put()
		self.redirect('/')
	    

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/edit', EditUser),
    ('/commit', CommitUser)
], debug=True)
