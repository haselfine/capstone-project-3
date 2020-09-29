from peewee import *

db = SqliteDatabase('artwork.sqlite', pragmas={'foreign_keys': 1})

class BaseModel(Model):
    class Meta:
        database = db

class Artist(BaseModel):
    artist_name = CharField(primary_key= True, unique=True)
    email = CharField()

    def __str__(self):
        return f'Name: {self.artist_name}. Email: {self.email}'

class Artwork(BaseModel):
    artist_name = ForeignKeyField(Artist, backref='artwork')
    artwork_name = CharField(unique=True)
    price = DecimalField()
    available = BooleanField()

    def __str__(self):
        return f'Artist name: {self.artist_name}. Artwork name: {self.artwork_name}. Price: ${self.price}. Available? {self.available}'

class Artist_Error(Exception):
    ''''''
    pass

class Artwork_Error(Exception):
    ''''''
    pass


db.connect()
db.create_tables([Artist, Artwork])