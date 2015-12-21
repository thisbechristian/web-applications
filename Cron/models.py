from google.appengine.ext import ndb

class Thing(ndb.Model):
	time = ndb.StringProperty()

class EmailConfig(ndb.Model):
	enabled = ndb.BooleanProperty()