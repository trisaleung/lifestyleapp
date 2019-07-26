import webapp2
from google.appengine.api import urlfetch, users
import json
import jinja2
import os
import random
from fatsecret import Fatsecret
from lifestyle_model import User, Meal

consumer_key = "2de49a3300b94286944e4cbae4986364"
consumer_secret = "95f02e15797b47d0b6560e15c4c86740"

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
        user = users.get_current_user()

        if user == None:
            self.redirect("/")
        else:
            life_key ="2de49a3300b94286944e4cbae4986364"
            fs = Fatsecret(consumer_key, consumer_secret)
            print(fs)
            log_template = the_jinja_env.get_template("/templates/log.html")

            print(fs.foods_search('bread'))


            amountofwater = 8
            logout_url = users.create_logout_url("/")

            life_key ="2de49a3300b94286944e4cbae4986364"
            # fs = Fatsecret(consumer_key, consumer_secret)
            # print(Fatsecret)
            user = users.get_current_user()
            logout_url = users.create_logout_url("/")
            template_vars = {

            "amountofwater" : "",
            "logout_url" : logout_url

            }
            log_template = the_jinja_env.get_template("/templates/log.html")

            self.response.write(log_template.render(template_vars))

    def post(self):
        amountofwater = self.request.get("amountofwater")
        logout_url = users.create_logout_url("/")

        template_vars = {
            "amountofwater" : amountofwater,
            "logout_url" : logout_url
        }
        log_template = the_jinja_env.get_template("/templates/log.html")

        self.response.write(log_template.render(template_vars))

class ProfileHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()

        if user == None:
            self.redirect("/")
        else:
            profile_template = the_jinja_env.get_template("/templates/profile.html")

            user = users.get_current_user()
            # nickname = user.nickname()
            # print nickname

            logout_url = users.create_logout_url("/")

            template_vars = {
                # "nickname" : nickname,
                "logout_url" : logout_url,
            }
            self.response.write(profile_template.render(template_vars))

        #not sure how you guys are doing the editing thing and if it needs a post or not

    def post(self):
        weight = self.request.get("weight")
        height = self.request.get("height")
        age = self.request.get("age")
        gender = self.request.get("gender")

        bmi = 16
        # bmi = ( weight / (height * height)) * 703
        wateramount = 8

        calories = 0

        if gender == "male":
            calories = 2000
        elif gender == "female":
            calories = 2000

        new_user = User(height=int(height), weight=int(weight), age=int(age), gender=gender, bmi=int(bmi), wateramount=int(wateramount),calories=int(calories))

        new_user.put()

        user_query = User.query().fetch()

        height = new_user.height
        weight = new_user.weight
        age = new_user.age
        gender = new_user.gender

        profile_template = the_jinja_env.get_template("/templates/profileComplete.html")

        user = users.get_current_user()
        # nickname = user.nickname()
        # print nickname

        logout_url = users.create_logout_url("/")

        template_vars = {
            # "nickname" : nickname,
            "logout_url" : logout_url,
            "usersWeight" : weight,
            "usersHeight" : height,
            "usersAge" : age,
            # "gender": usersGender
        }
        self.response.write(profile_template.render(template_vars))


app = webapp2.WSGIApplication([
    ("/", MainHandler),
    ("/log", LogHandler),
    ("/profile", ProfileHandler),
])
