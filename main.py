from menu import Menu

def main():
    menu = create_menu()

def create_menu():
    menu = Menu()
    menu.add_option(1, "Add artist", add_artist())
    return menu

main()