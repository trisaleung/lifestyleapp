import webapp2
from google.appengine.api import urlfetch, users
import json
import jinja2
import os
import random
from fatsecret import Fatsecret

from lifestyle_model import User, Meal

from lifestyle_model import User, Meal #api
from google.appengine.ext import ndb


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
            self.redirect("/profile")
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
            "logout_url" : logout_url,
            }
            log_template = the_jinja_env.get_template("/templates/log.html")

            #checks whether or not the user has an account here before
            user_id = user.user_id()


            #if the user does not, they are redirected to create a new account and enter new info
            if not User.get_by_user(user):
                self.redirect("/signup")

            else:
                life_key ="2de49a3300b94286944e4cbae4986364"
                fs = Fatsecret(consumer_key, consumer_secret)
                print(fs)
                log_template = the_jinja_env.get_template("/templates/log.html")
                print(self.request.get('#foods123'))
                print(fs.foods_search(self.request.get('#foods123')))

                logout_url = users.create_logout_url("/")

        life_key ="2de49a3300b94286944e4cbae4986364"
                # fs = Fatsecret(consumer_key, consumer_secret)
                # print(Fatsecret)
        user = users.get_current_user()
        logout_url = users.create_logout_url("/")
        # template_vars = {
        #         "amountofwater" : "",
        #         "logout_url" : logout_url,
        #         "calories" : calories
        #         }

    #shows your input after you submit
    def post(self):

        amountofwater = self.request.get("amountofwater")
        logout_url = users.create_logout_url("/")

        fs = Fatsecret(consumer_key, consumer_secret)
        print(fs)
        print(self.request.get('foods123'))

        # results = (fs.foods_search(self.request.get('foods123')))
        # print(results[0])

        calories = json.loads(results)
        print(calories)

        calories = (results[0]['food_description'])
        print(calories["food_description"])




        template_vars = {
            "amountofwater" : amountofwater,
            "logout_url" : logout_url,
            "calories" : calories
        }
        log_template = the_jinja_env.get_template("/templates/log.html")

        self.response.write(log_template.render(template_vars))




class SignUpHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()

        if user == None:
            self.redirect("/")
        else:
            user_template = the_jinja_env.get_template("/templates/profile.html")

            logout_url = users.create_logout_url("/")

            template_vars = {
                "logout_url" : logout_url
            }

            self.response.write(user_template.render(template_vars))

    def post(self):
        user = users.get_current_user()

        weight = self.request.get("weight")
        height = self.request.get("height")
        age = self.request.get("age")
        gender1 = self.request.get("gender1")
        gender2 = self.request.get("gender2")
        weightgoal = self.request.get("weightgoal")
        # weeklygoal = self.request.get("weeklymenu")
        calories = 0

        activitylevel = self.request.get("activitymenu")
        weeklytarget = self.request.get("weeklytargetmenu")

        weightconverted = float(weight) * 0.453592
        heightconverted = float(height) * 2.54

        gender = ""

        user_id = user.user_id()

        bmi = (float(weight) / (float(height) * float(height))) * 703

        if gender1 == "male":
            gender = gender1
            calories = (10 * weightconverted) + (6.25 * heightconverted) - (5 * int(age)) + 5

        elif gender2 == "female":
            gender = gender2
            calories = (10 * weightconverted)+ (6.25 * heightconverted) - (5 * int(age)) - 161

        if activitylevel == "a":
            calories = calories * 1.2
        elif activitylevel == "b":
            calories = calories * 1.37
        elif activitylevel == "c":
            calories = calories * 1.55
        elif activitylevel == "d":
            calories = calories * 1.725

        if weeklytarget == 1:
            calories = calories - 1000
        elif weeklytarget == 2:
            calories = calories - 750
        elif weeklytarget == 3:
            calories = calories - 500
        elif weeklytarget == 4:
            calories = calories - 250
        elif weeklytarget == 5:
            calories = calories + 250
        elif weeklytarget == 6:
            calories = calories + 500
        elif weeklytarget == 7:
            calories = calories + 750
        elif weeklytarget == 8:
            calories = calories + 1000

        #if activity level low: change calories
        #use constants, multiply it by the calories variable

        wateramount = 8

        new_user = User(user_id=user_id, height=int(height), weight=int(weight), age=int(age), gender=gender, bmi=float(bmi), wateramount=wateramount, calories=int(calories), weightgoal=int(weightgoal))

        new_user.put()

        user_query = User.query().fetch()

        height = new_user.height
        weight = new_user.weight
        age = new_user.age
        gender = new_user.gender
        bmi = new_user.bmi
        cupsofwater = new_user.wateramount
        goals = new_user.calories

        profile_template = the_jinja_env.get_template("/templates/profileComplete.html")

        user = users.get_current_user()


        logout_url = users.create_logout_url("/")

        template_vars = {

            "logout_url" : logout_url,
            "usersWeight" : weight,
            "usersHeight" : height,
            "usersAge" : age,
            "userBMI" : bmi,
            "userwater" : cupsofwater,
            "caloriegoals" : goals,
        }
        self.response.write(profile_template.render(template_vars))



#your profile. includes all the data you put in earlier (tied to your user_id). should eventually include an edit button so you can change your data.

class ProfileHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()

        if user == None:
            self.redirect("/")
        else:

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

            #     user_id = user.user_id()
            #
            # if not User.get_by_user(user):
            #     self.redirect("/signup")
            #
            # else:
            #     profile_template = the_jinja_env.get_template("/templates/profileComplete.html")

                #profileComplete.html is the actual profile with all of the data entered

                # user_query = User.query(ndb.GenericProperty("user_id")==user_id).fetch()
                # json = user_query
                # print(json)
                #
                # weight = json[0].weight
                # height = json[0].height
                # age = json[0].age
                # gender = json[0].gender
                # bmi = json[0].bmi
                # wateramount = json[0].wateramount
                # caloriesgoal = json[0].calories
                #
                #
                # logout_url = users.create_logout_url("/")
                #
                # template_vars = {
                #     # "nickname" : nickname,
                #     "logout_url" : logout_url,
                #     "usersWeight" : weight,
                #     "usersHeight" : height,
                #     "usersAge" : age,
                #     "userBMI" : bmi,
                #     "userwater" : wateramount,
                #     "caloriegoals" : caloriesgoal
                # }
                # self.response.write(profile_template.render(template_vars))

app = webapp2.WSGIApplication([
    ("/", MainHandler),
    ("/log", LogHandler),
    ("/profile", ProfileHandler),
    ("/signup", SignUpHandler)
])
