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

class MainHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            self.redirect("/pinenter")
        else:
            login_url = users.create_login_url("/")
            self.redirect(login_url)

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
            #print(self.request.get('#foods123'))
            #print(fs.foods_search(self.request.get('#foods123')))


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
        fs = Fatsecret(consumer_key, consumer_secret)
        print(fs)
        print('LogHandler.post')
        print(self.request.get('foods123'))
        print(fs.foods_search(self.request.get('foods123')))
        template_vars = {
            "amountofwater" : amountofwater,
            "logout_url" : logout_url
        }
        log_template = the_jinja_env.get_template("/templates/log.html")

        self.response.write(log_template.render(template_vars))

class SignUpHandler(webapp2.RequestHandler):
    def get(self):
        pass

    def post(self):
        pass

# class ProfileHandler(webapp2.RequestHandler):
#     def get(self):
#         user_query = User.query(User.pinNumber == pinentered).fetch()
#
#
#
#
#
#
#         user = users.get_current_user()
#
#         user_template = the_jinja_env.get_template("/templates/pinenter.html")
#
#         self.response.write(user_template.render())
#
#     def post(self):
#         pinentered = int(self.request.get("pinNumber"))
#
#         user_query = User.query(User.pinNumber == pinentered).fetch()
#
#         self.redirect("/log")

class ProfileHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()

        user_template = the_jinja_env.get_template("/templates/pinenter.html")

        self.response.write(user_template.render())

    def post(self):
        profile_template = the_jinja_env.get_template("/templates/profileComplete.html")

        pinentered = int(self.request.get("pinNumber"))
        user_query = User.query(User.pinNumber == pinentered).fetch()

        json = user_query

        weight = json[0].weight
        height = json[0].height
        age = json[0].age

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
        #
        #
        #
        # if user == None:
        #     self.redirect("/")
        # else:
        #     # if user.height == None and user.weight == None:
        #     profile_template = the_jinja_env.get_template("/templates/profile.html")
        #
        #     user = users.get_current_user()
        #     # nickname = user.nickname()
        #     # print nickname
        #
        #     logout_url = users.create_logout_url("/")
        #
        #     template_vars = {
        #         # "nickname" : nickname,
        #         "logout_url" : logout_url,
        #     }
        #     self.response.write(profile_template.render(template_vars))
            # else:
                # weight = self.request.get("weight")
                # height = self.request.get("height")
                # age = self.request.get("age")
                # gender = self.request.get("gender")
                # pin = self.request.get("pin")
                #
                # bmi = 16
                # # bmi = ( weight / (height * height)) * 703
                # wateramount = 8
                #
                # calories = 0
                #
                # if gender == "male":
                #     calories = 2000
                # elif gender == "female":
                #     calories = 2000
                #
                # new_user = User(height=int(height), weight=int(weight), age=int(age), gender=gender, bmi=int(bmi), wateramount=int(wateramount),calories=int(calories), pinNumber=int(pin))
                #
                # new_user.put()
                #
                # user_query = User.query().fetch()
                #
                # height = new_user.height
                # weight = new_user.weight
                # age = new_user.age
                # gender = new_user.gender
                #
                # profile_template = the_jinja_env.get_template("/templates/profileComplete.html")
                #
                # user = users.get_current_user()
                # # nickname = user.nickname()
                # # print nickname
                #
                # logout_url = users.create_logout_url("/")
                #
                # template_vars = {
                #     # "nickname" : nickname,
                #     "logout_url" : logout_url,
                #     "usersWeight" : weight,
                #     "usersHeight" : height,
                #     "usersAge" : age,
                #     # "gender": usersGender
                # }
                # self.response.write(profile_template.render(template_vars))

    # def post(self):
    #     weight = self.request.get("weight")
    #     height = self.request.get("height")
    #     age = self.request.get("age")
    #     gender = self.request.get("gender")
    #     pin = self.request.get("pin")
    #
    #     bmi = 16
    #     # bmi = ( weight / (height * height)) * 703
    #     wateramount = 8
    #
    #     calories = 0
    #
    #     if gender == "male":
    #         calories = 2000
    #     elif gender == "female":
    #         calories = 2000
    #
    #     new_user = User(height=int(height), weight=int(weight), age=int(age), gender=gender, bmi=int(bmi), wateramount=int(wateramount),calories=int(calories), pinNumber=int(pin))
    #
    #     new_user.put()
    #
    #     user_query = User.query().fetch()
    #
    #     height = new_user.height
    #     weight = new_user.weight
    #     age = new_user.age
    #     gender = new_user.gender
    #
    #     profile_template = the_jinja_env.get_template("/templates/profileComplete.html")
    #
    #     user = users.get_current_user()
    #     # nickname = user.nickname()
    #     # print nickname
    #
    #     logout_url = users.create_logout_url("/")
    #
    #     template_vars = {
    #         # "nickname" : nickname,
    #         "logout_url" : logout_url,
    #         "usersWeight" : weight,
    #         "usersHeight" : height,
    #         "usersAge" : age,
    #         # "gender": usersGender
    #     }
    #     self.response.write(profile_template.render(template_vars))

app = webapp2.WSGIApplication([
    ("/", MainHandler),
    ("/log", LogHandler),
    ("/profile", ProfileHandler),
    ("/signup", SignUpHandler)
])
