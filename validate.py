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