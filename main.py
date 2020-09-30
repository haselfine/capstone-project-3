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
        return validate.validate_artist()
    elif user_choice == '2':
        return validate.validate_artwork()
    elif user_choice == '3' or user_choice == '4':
        artist = input('Enter the name of the artist who made the artwork: ')
        db_validity = validate.is_artist_in_db(artist)
        if db_validity and user_choice == '3':
            view.response(f'Artist: {artist}')
            view.array_response(vm.get_all_artwork(artist))
            return ''
        elif db_validity and user_choice == '4':
            view.array_response(vm.get_all_available_artwork(artist))
            return ''
    #TODO add delete option

if __name__ == '__main__':
    main()