from model import *

class ViewModel:

    def add_artist(self, name_in, email_in):
        artist = Artist.create(artist_name=name_in, email=email_in)
        return artist

    def add_artwork(self, artist_name_in, artwork_name_in, price_in, available_in):
        artwork = Artwork.create(artist_name=artist_name_in, artwork_name=artwork_name_in, price=price_in, available=available_in)
        return artwork

    def get_all_artwork(self, artist_in):
        return Artwork.select().where(Artwork.artist_name == artist_in)

    def get_all_available_artwork(self, artist_in):
        return Artwork.select().where(Artwork.artist_name == artist_in, Artwork.available == True)

    def delete_artwork(self, artwork_name_in):
        return Artwork.delete().where(Artwork.artwork_name == artwork_name_in)