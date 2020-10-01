from model import *



def add_artist(name_in, email_in):
    try:
        artist = Artist.create(artist_name=name_in, email=email_in)
        artist.save()
        return 'Artist saved.'
    except (DatabaseError):
        print(DatabaseError)
        return f'There was an error in adding the artist. Make sure {name_in} isn\'t already in database.'

def add_artwork(artist_id_in, artwork_name_in, price_in, available_in):
    try:
        print(available_in)
        artwork = Artwork.create(artist_id=artist_id_in, artwork_name=artwork_name_in, price=price_in, available=available_in)
        artwork.save()
        print(artwork)
        return 'Artwork saved.'
    except (DatabaseError):
        return f'There was an error in adding the artist. Make sure {artwork_name_in} isn\'t already in database.'

def find_artist(artist_name_in):
    try:
        searched_artist = Artist.get_or_none(Artist.artist_name == artist_name_in)
        return searched_artist
    except (DatabaseError):
        return 'Sorry. There was an error retrieving the artist.'

def find_artwork(artist_id_in, artwork_name_in):
    try:
        searched_artwork = Artwork.get_or_none(Artwork.artist_id == artist_id_in, Artwork.artwork_name == artwork_name_in)
        return searched_artwork
    except (DatabaseError):
        return 'Sorry. There was an error retrieving the artwork.'

def get_all_artwork(artist_id_in):
    try:
        return Artwork.select().join(Artist, on=(Artist.artist_id == Artwork.artist_id)).where(Artwork.artist_id == artist_id_in)
    except(DatabaseError):
        return 'Sorry. There was an error retrieving the artwork'


def get_all_available_artwork(artist_id_in):
    try:
        return Artwork.select().where(Artwork.artist_id == artist_id_in, Artwork.available == 1)
    except(DatabaseError):
        return 'Sorry. There was an error retrieving the artwork'

def delete_artwork(artist_id_in, artwork_name_in):
    try:
        return Artwork.delete().where(Artwork.artist_id == artist_id_in, Artwork.artwork_name == artwork_name_in).execute()
    except(DatabaseError):
        return 'Sorry. There was an error deleting the artwork'