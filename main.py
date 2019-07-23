import webapp2
from google.appengine.api import urlfetch
import json
import jinja2
import os
import random

the_jinja_env = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions = ['jinja2.ext.autoescape'],
    undefined = jinja2.StrictUndefined,
    autoescape = True
)

class MainHandler(webapp2.RequestHandler):
    def get(self):
        pass

    def post(self):
        pass

class LogHandler(webapp2.RequestHandler):
    def get(self):
        pass

    def post(self):
        pass

app = webapp2.WSGIApplication([
    ("/", MainHandler),
    ("/log", LogHandler),
])
