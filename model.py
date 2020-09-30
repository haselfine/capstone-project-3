from peewee import *

db = SqliteDatabase('artwork.sqlite', pragmas={'foreign_keys': 1})

class BaseModel(Model):
    class Meta:
        database = db

class Artist(BaseModel):
    artist_name = CharField(primary_key= True, unique=True, constraints=[Check('length(artist_name) >= 1]'), Check('artist_name is not null')])
    email = CharField(unique=True, constraints=[Check('length(email) >= 1]'), Check('email is not null')])

    def __str__(self):
        return f'Name: {self.artist_name}. Email: {self.email}'

class Artwork(BaseModel):
    artist_name = ForeignKeyField(Artist, backref='artwork')
    artwork_name = CharField(constraints=[Check('length(artwork_name) >= 1]'), Check('artwork_name is not null')])
    price = DecimalField(constraints=[Check('price >= 0'), Check('price < 1000000.01')])
    available = BooleanField(default=True)

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