from menu import Menu
from view import View
from viewmodel import ViewModel as vm

def main():
    menu = create_menu()

    while True:
        user_choice = View()

    

def create_menu():
    menu = Menu()
    menu.add_option(1, "Add artist", vm.add_artist)
    menu.add_option(2, "Add artwork", vm.add_artwork)
    menu.add_option(3, "Get all artwork (available and unavailable)", vm.get_all_artwork)
    menu.add_option(4, "Get all available artwork", vm.get_all_available_artwork)
    menu.add_option(5, "Delete an artwork", vm.delete_artwork)
    return menu


main()