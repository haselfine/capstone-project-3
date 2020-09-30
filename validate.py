import view
import viewmodel as vm

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
