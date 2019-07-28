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
                template_vars = {
                "amountofwater" : "",
                "logout_url" : logout_url
                }

    #shows your input after you submit
    def post(self):

        amountofwater = self.request.get("amountofwater")
        logout_url = users.create_logout_url("/")

        fs = Fatsecret(consumer_key, consumer_secret)
        print(fs)
        print(self.request.get('foods123'))

        results = (fs.foods_search(self.request.get('foods123')))
        print(results[0])

        calories = (results[0]['food_description'])
        print(calories)

        calories = Fatsecret.valid_response(results[0])













        # print(fs.foods_search(self.request.get('foods123')))
        #
        # user_query = User.query(ndb.GenericProperty("user_id")==user_id).fetch()
        # json = user_query
        #
        # caloriesgoal = json[0].calories


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
        weeklygoal = self.request.get("weeklymenu")

        gender = ""

        if gender2 == None:
            gender = gender1
        elif gender1 == None:
            gender = gender2

        # weightgoal = self.request.get("weightgoal")
        # weeklytarget = self.request.get()
        user_id = user.user_id()

        bmi = 16
        # bmi = ( weight / (height * height)) * 703
        wateramount = 8

        calories = 0

        # if gender == "male":
        #     calories = 2000
        # elif gender == "female":
        #     calories = 2000



        new_user = User(user_id=user_id, height=int(height), weight=int(weight), age=int(age), gender=gender)

        new_user.put()

        user_query = User.query().fetch()

        height = new_user.height
        weight = new_user.weight
        age = new_user.age
        gender = new_user.gender







        profile_template = the_jinja_env.get_template("/templates/profileComplete.html")

        user = users.get_current_user()


        logout_url = users.create_logout_url("/")

        template_vars = {

            "logout_url" : logout_url,
            "usersWeight" : weight,
            "usersHeight" : height,
            "usersAge" : age,
            # "gender": usersGender
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
=======
            user_id = user.user_id()

            if not User.get_by_user(user):
                self.redirect("/signup")

            else:
                profile_template = the_jinja_env.get_template("/templates/profileComplete.html")

                #profileComplete.html is the actual profile with all of the data entered

                user_query = User.query(ndb.GenericProperty("user_id")==user_id).fetch()
                json = user_query
                print(json)

                weight = json[0].weight
                height = json[0].height
                age = json[0].age
                gender = json[0].gender
                bmi = json[0].bmi
                wateramount = json[0].wateramount
                caloriesgoal = json[0].calories


                logout_url = users.create_logout_url("/")

                template_vars = {
                    # "nickname" : nickname,
                    "logout_url" : logout_url,
                    "usersWeight" : weight,
                    "usersHeight" : height,
                    "usersAge" : age,
                    "userBMI" : bmi,
                    "userwater" : wateramount,
                    "caloriegoals" : caloriesgoal
                }
                self.response.write(profile_template.render(template_vars))

app = webapp2.WSGIApplication([
    ("/", MainHandler),
    ("/log", LogHandler),
    ("/profile", ProfileHandler),
    ("/signup", SignUpHandler)
])
