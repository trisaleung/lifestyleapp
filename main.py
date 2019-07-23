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

app = webapp2.WSGIApplication([
    ("/", MainHandler),
])

class MainHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if  user:
        #     self.response.write("Now is the winter of our discontent")
        # else:
            self.redirect("/loggedin")
        else:
            self.redirect("/nouser")

class NoUserHandler(webapp2.RequestHandler):
    def get(self):
        login_url = users.create_login_url("/")
        self.response.write('Login here: <a href="' + login_url + '">click here</a>')

class LoggedInHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        nickname = user.nickname()

        logout_url = users.create_logout_url("/")
        self.response.write("Hello " + nickname + '. <a href="' + logout_url + '">Logout here</a>')

app = webapp2.WSGIApplication([
    ("/", MainHandler),
    ("/nouser", NoUserHandler),
    ("/loggedin", LoggedInHandler)
], debug=True)
