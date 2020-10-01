import view
import viewmodel as vm
import re

def is_valid_choice(choice):
    choices = ['1', '2', '3', '4', '5', 'Q']
    if choice in choices:
        return True
    else:
        return False

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
    if len(str(price)) <= 0:
        return False
    elif price <= 0:
        return False
    elif price >= 1000000.01:
        return False
    else:
        return True

def is_artist_in_db(artist):
    artist_info = []
    artist_in_db = vm.find_artist(artist)
    if artist_in_db == None:
        artist_info = [False]
        return artist_info
    else:
        artist_info = [True, artist_in_db.artist_id]
        return artist_info

def is_artwork_in_db(artist, artwork):
    artwork_in_db = vm.find_artwork(artist, artwork)
    if artwork_in_db == None:
        return False
    else:
        return True

def is_valid_email(email):
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$' #found at https://www.geeksforgeeks.org/check-if-email-address-valid-or-not-in-python/
    return re.search(regex, email)

def is_available(availability):
    if availability == 'y':
        return 1
    elif availability == 'n':
        return 0
    else:
        return -1

def validate_artist():
    artist_info = []
    artist_to_add = input('Enter the name of the artist to add: ')
    if is_valid_artist(artist_to_add):
        email_to_add = input('Enter the email of the artist: ')
        if is_valid_email(email_to_add):
            artist_info = ['artist-success', artist_to_add, email_to_add]
            return artist_info
        else:
            artist_info = ['Email must be in xxxx@yyy.com format. Try again.']
            return artist_info
    else:
        artist_info = ['Artist must have at least one letter. Try again.']
        return artist_info
    

def validate_artwork():
    artwork_info = []
    artist_info = validate_artist_db()
    if artist_info[0]:
        artwork_to_add = str(input('Enter the name of the artwork: '))
        if is_valid_artwork(artwork_to_add):
            price_to_add = float(input('Enter the price of the artwork: '))
            if is_valid_price(price_to_add):
                availability_to_add = input('Is the artwork available? Type "y" for yes or "n" for no. ')
                if is_available(availability_to_add) != -1:
                    print(is_available(availability_to_add))
                    artwork_info = ['artwork-success', artist_info[1], artwork_to_add, price_to_add, is_available(availability_to_add)]
                    return artwork_info
                else:
                    artwork_info = ['Availability must be "y" or "n"']
                    return artwork_info
            else:
                artwork_info = ['Price must be in digit form and a positive number less than or equal to one million.']
                return artwork_info
        else:
            artwork_info = ['Artwork must have at least one character in name.']
            return 
    else:
        artwork_info = ['Artist not found. Try again.']
        return artwork_info

def validate_artist_db():
    artist = input('Enter the name of the artist who made the artwork: ')
    db_validity_and_artist = is_artist_in_db(artist)
    return db_validity_and_artist

def validate_artwork_db(artist_id):
    artwork = input('Enter the name of the artwork: ')
    db_validity = is_artwork_in_db(artist_id, artwork)
    db_validity_and_artwork = [db_validity, artwork]
    return db_validity_and_artwork

def are_you_sure(choice):
    while True:
        yes_or_no = input(f'Are you sure you would like to {choice}? y or n: ')
        if yes_or_no == 'y':
            return True
        elif yes_or_no == 'n':
            return False
        else:
            print('You must either answer y or n')