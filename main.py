from menu import Menu
import view
import viewModel as vm
import validate

def main():
    menu = create_menu()

    while True:
        user_choice = view.get_menu_choice(menu)
        if validate.validate_input(user_choice):
            menu_action = menu.get_action(user_choice)
            menu_action()

def create_menu():
    menu = Menu()
    menu.add_option(1, "Add artist")
    menu.add_option(2, "Add artwork")
    menu.add_option(3, "Get all artwork (available and unavailable)")
    menu.add_option(4, "Get all available artwork")
    menu.add_option(5, "Delete an artwork")
    return menu

def validate_input(user_choice):
    if user_choice == 1:
        
        validate_artist()
    elif user_choice == 2:
        artist = input('Enter the name of the artist who made the artwork: ')
        if validate.is_artist_in_db(artist):
            
    elif user_choice == 3 or user_choice == 4:
        artist = input('Enter the name of the artist who made the artwork: ')
        return is_artist_in_db(artist)

def validate_artist():
    artist_to_add = input('Enter the name of the artist to add: ')
    artist_validity = is_valid_artist(artist_to_add)
    if artist_validity == False:
        view.response('artist')
    return artist_to_add

def validate_artwork(artist):
    artwork_to_add = input('Enter the name of the artwork to add: ')
    artwork_validity = is_valid_artwork(artwork_to_add)
    if artwork_validity == False:
        view.response('artwork')
    return artwork_validity, artwork_to_add

main()