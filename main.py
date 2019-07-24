import webapp2
from google.appengine.api import urlfetch, users
import json
import jinja2
import os
import random
# from fatsecret import Fatsecret


the_jinja_env = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions = ['jinja2.ext.autoescape'],
    undefined = jinja2.StrictUndefined,
    autoescape = True
)

# jinja_current_directory = jinja2.Environment(
#     loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
#     extensions=['jinja2.ext.autoescape'],
#     autoescape=True
# )

class MainHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            self.redirect("/profile")
        else:
            login_url = users.create_login_url("/")
            self.redirect(login_url)

# class NoUserHandler(webapp2.RequestHandler):
#     def get(self):
#         login_url = users.create_login_url("/")
#         start_template=the_jinja_env.get_template("templates/login.html")
#         self.response.write('<a href="' + login_url + '">click here</a>')


class LoggedInHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        nickname = user.nickname()

        logout_url = users.create_logout_url("/")
        self.response.write("Hello " + nickname + '. <a href="' + logout_url + '">Logout here</a>')

class LogHandler(webapp2.RequestHandler):
    def get(self):
        # life_key ="2de49a3300b94286944e4cbae4986364"
        # fs = Fatsecret(consumer_key, consumer_secret)
        # print(Fatsecret)
        log_template = the_jinja_env.get_template("/templates/log.html")

        amountofwater = 8

        life_key ="2de49a3300b94286944e4cbae4986364"
        # fs = Fatsecret(consumer_key, consumer_secret)
        # print(Fatsecret)
        template_vars = {
        "amountofwater" : ""
        }
        log_template = the_jinja_env.get_template("/templates/log.html")

        self.response.write(log_template.render(template_vars))

    def post(self):
        amountofwater = self.request.get("amountofwater")

        template_vars = {
            "amountofwater" : amountofwater
        }
        log_template = the_jinja_env.get_template("/templates/log.html")

        self.response.write(log_template.render(template_vars))

class ProfileHandler(webapp2.RequestHandler):
    def get(self):
        profile_template = the_jinja_env.get_template("/templates/profile.html")

        user = users.get_current_user()
        nickname = user.nickname()
        # print nickname

        logout_url = users.create_logout_url("/")

        #hopefully once you log in, you'll be redirected to the templates page
        #and it will fill in your nickname and have a logout url

        template_vars = {
            "nickname" : nickname,
            "logout_url" : logout_url,
        }

        self.response.write(profile_template.render(template_vars))

        #not sure how you guys are doing the editing thing and if it needs a post or not

app = webapp2.WSGIApplication([
    ("/", MainHandler),
    ("/log", LogHandler),
    ("/profile", ProfileHandler),
])
