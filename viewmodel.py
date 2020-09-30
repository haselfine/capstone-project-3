from model import *



def add_artist(name_in, email_in):
    try:
        artist = Artist.create(artist_name=name_in, email=email_in)
        artist.save()
        return 'Artist saved.'
    except (DatabaseError):
        return 'There was an error in adding the artist.'

def add_artwork(artist_name_in, artwork_name_in, price_in, available_in):
    try:
        artwork = Artwork.create(artist_name=artist_name_in, artwork_name=artwork_name_in, price=price_in, available=available_in)
        artwork.save()
        return 'Artwork saved.'
    except:
        return 'There was an error in adding the artwork'

def find_artist(artist_name_in):
    searched_artist = Artist.get_or_none(Artist.artist_name == artist_name_in)
    return searched_artist

def get_all_artwork(artist_in):
    return Artwork.select().where(Artwork.artist_name == artist_in)

def get_all_available_artwork(artist_in):
    return Artwork.select().where(Artwork.artist_name == artist_in, Artwork.available == True)

def delete_artwork(artwork_name_in):
    return Artwork.delete().where(Artwork.artwork_name == artwork_name_in)