from google.appengine.ext import db

class Todo(db.Model):
    content = db.StringProperty()
    done    = db.BooleanProperty()
    order   = db.IntegerProperty()
