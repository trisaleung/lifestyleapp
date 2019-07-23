import webapp2
from google.appengine.api import urlfetch, users
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

jinja_current_directory = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainHandler(webapp2.RequestHandler):
    def get(self):
        pass

    def post(self):
        pass

class LogHandler(webapp2.RequestHandler):
    def get(self):
        log_template = the_jinja_env.get_template("/templates/log.html")
        self.response.write(log_template.render())

    def post(self):
        pass

class LoggedInHandler(webapp2.RequestHandler):
    def get(self):
        pass

    def post(self):
        pass

app = webapp2.WSGIApplication([
    ("/", MainHandler),
    ("/log", LogHandler),
    ("/loggedin", LoggedInHandler),
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
        start_template=jinja_current_directory.get_template("templates/login.html")
        self.response.write(start_template.render())

class LoggedInHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        nickname = user.nickname()

        logout_url = users.create_logout_url("/")
        self.response.write("Hello " + nickname + '. <a href="' + logout_url + '">Logout here</a>')
