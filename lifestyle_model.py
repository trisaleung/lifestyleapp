from google.appengine.ext import ndb

class User(ndb.Model):
    user_id = ndb.StringProperty(required=True)
    height = ndb.IntegerProperty(required=True)
    weight = ndb.IntegerProperty(required=True)
    age = ndb.IntegerProperty(required=True)
    gender = ndb.StringProperty(required=True)
    bmi = ndb.FloatProperty(required=True)
    wateramount = ndb.IntegerProperty(required=True)
    calories = ndb.IntegerProperty(required=True)
    weightgoal = ndb.IntegerProperty(required=True)
    weeklytarget = ndb.IntegerProperty(required=True)

    #functions inside of object; cls represents class
    @classmethod
    def get_by_user(cls, user):
        return cls.query().filter(cls.user_id == user.user_id()).get()

class Meal(ndb.Model):
    mealname = ndb.StringProperty(required=True)
    calories = ndb.IntegerProperty(required=True)

class Water(ndb.Model):
    waternumber = ndb.IntegerProperty(required=True)
#
# class Day(ndb.Model):
#     meals = ndbKeyProperty(Meal, repeated=True)
