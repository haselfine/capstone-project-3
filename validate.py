import view
import viewmodel as vm
import re

def is_valid_artist(artist):
    if len(artist.strip()) <= 0:
        return False
    elif artist.isdigit():
        return False
    else:
        return True

def is_valid_artwork(artwork):
    if len(artwork.strip()) <= 0:
        return False
    else:
        return True

def is_valid_price(price):
    if len(price.strip()) <= 0:
        return False
    elif price <= 0:
        return False
    elif price >= 1000000.01:
        return False
    else:
        return True

def is_artist_in_db(artist):
    artist_in_db = vm.find_artist(artist)
    if artist_in_db == None:
        view.response('no_artist')
        return False
    else:
        return True

def is_valid_email(email):
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$' #found at https://www.geeksforgeeks.org/check-if-email-address-valid-or-not-in-python/
    return re.search(regex, email)

def is_available(availability):
    if availability == 'y':
        return True
    elif availability == 'n':
        return False
    else:
        return 'Invalid'

def validate_artist():
    artist_to_add = input('Enter the name of the artist to add: ')
    if is_valid_artist(artist_to_add):
        email_to_add = input('Enter the email of the artist: ')
        if is_valid_email(email_to_add):
            return vm.add_artist(artist_to_add, email_to_add)
        else:
            return 'Email must be in xxxx@yyy.com format. Try again.'
    else:
        return 'Artist must have at least one letter. Try again.'
    

def validate_artwork():
    artist = input('Enter the name of the artist who made the artwork: ')
    if is_artist_in_db(artist):
        artwork_to_add = str(input('Enter the name of the artwork: '))
        if is_valid_artwork(artwork_to_add):
            price_to_add = float(input('Enter the price of the artwork: '))
            if is_valid_price(price_to_add):
                availability_to_add = input('Is the artwork available? Type "y" for yes or "n" for no. ')
                if is_available(availability_to_add) != 'Invalid':
                    return vm.add_artwork(artist, artwork_to_add, price_to_add, availability_to_add)
                else:
                    return 'Availability must be "y" or "n"'
            else:
                return 'Price must be in digit form and a positive number less than or equal to one million.'
        else:
            return 'Artwork must have at least one character in name.'
    else:
        return 'Artist not found. Try again.'
