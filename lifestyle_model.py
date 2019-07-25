from google.appengine.ext import ndb

class User(ndb.Model):
    # username = ndb.StringProperty(required=True)
    # password = ndb.StringProperty(required=True)
    height = ndb.IntegerProperty(required=True)
    weight = ndb.IntegerProperty(required=True)
    age = ndb.IntegerProperty(required=True)
    gender = ndb.StringProperty(required=True)
    bmi = ndb.IntegerProperty(required=True)
    wateramount = ndb.IntegerProperty(required=True)
    calories = ndb.IntegerProperty(required=True)

class Meal(ndb.Model):
    user = ndb.KeyProperty(User)
    mealname = ndb.StringProperty(required=True)
    calories = ndb.IntegerProperty(required=True)
