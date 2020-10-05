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
    if len(artist.strip()) <= 0: #make sure artist name is not empty space
        return False
    elif artist.isdigit(): #make sure it isn't an int or float
        return False
    else:
        return True

def is_valid_artwork(artwork):
    if len(artwork.strip()) <= 0: #make sure it isn't empty space (I allow numbers here. They'll just be converted to a string)
        return False
    else:
        return True

def is_valid_price(price):
    if isinstance(price, int) or isinstance(price, float): #checks if it's an int or float
        is_number = True
    if len(str(price)) >= 0 and price >= 0 and price <= 1000000 and is_number: #price must not be empty, negative, or over a million dollars (this is a small art shop)
        return True
    else:
        return False

def is_artist_in_db(artist):
    artist_info = []
    artist_in_db = vm.find_artist(artist) #I wanted to avoid contacting the viewmodel from here, but it made more logical sense in the moment to have this function here
    if artist_in_db is None: #check for nonetype
        artist_info = [False] #send back in list form since the other return needs to be one
        return artist_info
    else:
        artist_info = [True, artist_in_db.artist_id] #artist is in database, return id as well
        return artist_info

def is_artwork_in_db(artist, artwork):
    artwork_in_db = vm.find_artwork(artist, artwork) #same as is_artist except it doesn't return anything other than true or false
    if artwork_in_db is None:
        return False
    else:
        return True

def is_valid_email(email): #use regex to make sure email is in correct format
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$' #found at https://www.geeksforgeeks.org/check-if-email-address-valid-or-not-in-python/
    return re.search(regex, email)

def convert_available(availability): #convert user input from y/n to the response the database is expecting 0 or 1
    if availability == 'y':
        return 1
    elif availability == 'n':
        return 0
    else:
        return -1 #doesn't send to database. Just means failure

def validate_artist():
    '''This functions walks the user through inputs to be validated.
    If the user fails to respond correctly, this returns an error message for them'''
    
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
    '''same as above except with artwork'''
    
    artwork_info = []
    artist_info = validate_artist_db()
    if artist_info[0]:
        artwork_to_add = str(input('Enter the name of the artwork: '))
        if is_valid_artwork(artwork_to_add):
            price_to_add = int(input('Enter the price of the artwork: '))
            if is_valid_price(price_to_add):
                availability_to_add = input('Is the artwork available? Type "y" for yes or "n" for no. ')
                if convert_available(availability_to_add) != -1:
                    artwork_info = ['artwork-success', artist_info[1], artwork_to_add, price_to_add, convert_available(availability_to_add)]
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