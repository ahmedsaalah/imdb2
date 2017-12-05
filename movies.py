from importall import *
class movies(db.Model):
   id = db.Column('movie_id', db.Integer, primary_key = True)
   name = db.Column(db.String(100))
   storyLine = db.Column(db.String(100))  
   thumbimage = db.Column(db.String(200))
   trailer = db.Column(db.String(50))


def __init__(self, name, storyLine, thumbimage, trailer ):
   self.name = name
   self.storyLine = storyLine
   self.thumbimage = thumbimage
   self.trailer = trailer

