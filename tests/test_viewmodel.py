from unittest import TestCase
import config
config.db_path = 'test_artwork.sqlite'
import models
from models import Artist, Artwork
import viewmodel

MODELS = [Artist, Artwork]

class TestArtworkDB(TestCase):

    def add_drop(self): #empty database
        models.db.drop_tables(MODELS)
        models.db.create_tables(MODELS)

    def add_example_artwork(self):
        '''This creates an artist and artwork which satisfy the requirements of the database'''
        self.add_drop()
        viewmodel.add_artist('Yoshitaka Amano', 'yamano@gmail.com')
        artwork_in = 'Final Fantasy VI Cover Art'
        price_in = 50
        available_in = False

        self.artist = viewmodel.find_artist('Yoshitaka Amano')
        viewmodel.add_artwork(self.artist.id, artwork_in, price_in, available_in)
        

    def test_add_artist_good_data(self):
        self.add_drop()
        artist_in = 'Yoshitaka Amano' #data that won't break it
        email_in = 'yamano@gmail.com'
        
        self.assertEqual('Artist saved.', viewmodel.add_artist(artist_in, email_in))

    def test_add_artist_duplicate_artist(self):
        self.add_drop()
        artist_in = 'Van Gogh'
        email_in = 'vgogh@gmail.com'

        viewmodel.add_artist(artist_in, email_in) #add artist once

        self.assertNotEqual('Artist saved.', viewmodel.add_artist(artist_in, email_in)) #try to add artist again. causes exception

    def test_add_artist_empty_name(self):
        self.add_drop()
        artist_in = '' #empty name will not be accepted
        email_in = 'vgogh@gmail.com'

        self.assertNotEqual('Artist saved.', viewmodel.add_artist(artist_in, email_in))

    def test_add_artist_empty_email(self):
        self.add_drop()
        artist_in = 'Van Gogh'
        email_in = '' #empty email will not be accepted

        self.assertNotEqual('Artist saved.', viewmodel.add_artist(artist_in, email_in))


    def test_add_artwork_good_data(self):
        self.add_drop()
        viewmodel.add_artist('Yoshitaka Amano', 'yamano@gmail.com')
        artwork_in = 'Final Fantasy VI Cover Art'
        price_in = 50
        available_in = False
        self.artist = viewmodel.find_artist('Yoshitaka Amano')
        
        self.assertEqual('Artwork saved.', viewmodel.add_artwork(self.artist.artist_id, artwork_in, price_in, available_in))

    def test_add_artwork_nonexistent_artist(self):
        self.add_drop()
        artist_id = 99999999 #there is no artist in database with this id
        artwork_in = 'asdf'
        price_in = 500
        available_in = True

        self.assertNotEqual('Artwork saved.', viewmodel.add_artwork(artist_id, artwork_in, price_in, available_in)) #not equal, not saved

    def test_add_artwork_bad_price(self):
        self.add_drop()
        viewmodel.add_artist('Yoshitaka Amano', 'yamano@gmail.com')
        artwork_in = 'Cloud Concept Art'
        available_in = True

        self.artist = viewmodel.find_artist('Yoshitaka Amano')
        self.assertNotEqual('Artwork saved.', viewmodel.add_artwork(self.artist.artist_id, artwork_in, '$50', available_in)) #try string
        self.assertNotEqual('Artwork saved.', viewmodel.add_artwork(self.artist.artist_id, artwork_in, -5000000, available_in)) #try negative
        self.assertNotEqual('Artwork saved.', viewmodel.add_artwork(self.artist.artist_id, artwork_in, 999999999, available_in)) #try over a million
        self.assertNotEqual('Artwork saved.', viewmodel.add_artwork(self.artist.artist_id, artwork_in, -0.0000001, available_in)) #try close to zero

    def test_find_artist_nonexistent(self):
        self.add_drop()
        self.assertIsNone(viewmodel.find_artist('asdf')) #no artists in database, will return None
        viewmodel.add_artist('lkjfei', 'weroiuwo23234398@aksjdfls.com')
        self.assertIsNone(viewmodel.find_artist('')) #even with an artist in the database, this will return None

    def test_find_artwork_good_data(self):
        self.add_drop()
        viewmodel.add_artist('Yoshitaka Amano', 'yamano@gmail.com')
        viewmodel.add_artwork(1, 'Yuffie Concept Art', 100, False)
        artwork_output = viewmodel.find_artwork(1, 'Yuffie Concept Art')
        self.assertIsInstance(artwork_output, Artwork)

    def test_get_all_artwork_good_data(self):
        self.add_example_artwork()
        self.assertNotEqual('Sorry. There was an error retrieving the artwork', viewmodel.get_all_artwork(1)) #passes

    def test_get_all_artwork_bad_data(self):
        self.add_example_artwork()
        self.assertEqual('Sorry. There was an error retrieving the artwork', viewmodel.get_all_artwork(999999)) #no artist with that id

    def test_get_available_artwork_good_data(self):
        self.add_example_artwork() #the artwork in here is unavailable
        self.assertEqual(0, len(viewmodel.get_all_available_artwork(1))) #so when searched, it doesn't come up
        
        viewmodel.add_artist('asdf', 'asdf@yyyy.com')
        artist = viewmodel.find_artist('asdf')
        viewmodel.add_artwork(artist.artist_id, 'l;kj', 20000, True)
        self.assertEqual(1, len(viewmodel.get_all_available_artwork(artist.artist_id))) #now there is an available artwork, so it returns that data

    def test_get_available_artwork_bad_data(self):
        self.add_drop()
        self.assertEqual(0, len(viewmodel.get_all_available_artwork('asfdsfalksdjfw'))) #this is expecting an integer, so the string will cause an exception


    def test_delete_artwork_good_data(self):
        self.add_example_artwork()
        artist = viewmodel.find_artist('Yoshitaka Amano')
        self.assertEqual(1, viewmodel.delete_artwork(artist.artist_id, 'Final Fantasy VI Cover Art')) #returns that 1 row was deleted

    def test_delete_artwork_bad_data(self):
        self.add_drop()
        self.assertEqual(0, viewmodel.delete_artwork('23432490000', 2304938)) #artwork is expecting an artist id as the first argument, title second