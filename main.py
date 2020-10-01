from menu import Menu
import view
import viewmodel as vm
import validate

def main():
    menu = create_menu()

    while True:
        user_choice = view.get_menu_choice(menu)
        if user_choice.upper() == 'Q':
            break
        valid_response = validate_input(user_choice)
        view.response(valid_response + '\n')

def create_menu():
    menu = Menu()
    menu.add_option('1', "Add artist")
    menu.add_option('2', "Add artwork")
    menu.add_option('3', "Get all artwork (available & unavailable)")
    menu.add_option('4', "Get all available artwork")
    menu.add_option('5', "Delete an artwork")
    menu.add_option('Q', "Quit")
    return menu

def validate_input(user_choice):
    if user_choice == '1':
        artist_info = validate.validate_artist()
        if artist_info[0] == 'artist-success':
            return vm.add_artist(artist_info[1], artist_info[2])
        else:
            return artist_info[0]
    elif user_choice == '2':
        artwork_info = validate.validate_artwork()
        if artwork_info[0] == 'artwork-success':
            return vm.add_artwork(artwork_info[1], artwork_info[2], artwork_info[3], artwork_info[4])
        else:
            return artwork_info[0]
    elif user_choice == '3' or user_choice == '4':
        db_validity_and_artist = validate.validate_artist_db()
        if db_validity_and_artist[0] and user_choice == '3':
            artwork_string = stringify_artwork(listify_artwork(vm.get_all_artwork(db_validity_and_artist[1])))
            return artwork_string
        elif db_validity_and_artist[0] and user_choice == '4':
            artwork_string = stringify_artwork(listify_artwork(vm.get_all_available_artwork(db_validity_and_artist[1])))
            return artwork_string
        else:
            return 'Could not find that artist'
    elif user_choice == '5':
        db_validity_and_artist = validate.validate_artist_db()
        if db_validity_and_artist[0]:
            db_validity_and_artwork = validate.validate_artwork_db(db_validity_and_artist[1])
            if db_validity_and_artwork[0]:
                if validate.are_you_sure('delete the artwork'):
                    vm.delete_artwork(db_validity_and_artist[1], db_validity_and_artwork[1])
                    return f'{db_validity_and_artwork[1]} was deleted.'
                else:
                    return 'Artwork was not deleted.'
            else:
                return f'Could not find artwork named "{db_validity_and_artwork[1]}" by {db_validity_and_artwork[1]}.'
        else:
            return f'Could not find artist {db_validity_and_artist[1]}.'



def listify_artwork(artwork_obj):
    artwork_list = []
    for artwork in artwork_obj:
        artwork_string = f'Name: {artwork.artwork_name} | Price: {artwork.price} | Available? {artwork.available}'
        artwork_list.append(artwork_string)
    return artwork_list

def stringify_artwork(artwork_list):
    return '\n'.join(artwork_list)


if __name__ == '__main__':
    main()