import viewmodel as vm
import validate

def get_menu_choice(menu): #print menu choice
    while True:
        print(menu)
        choice = input('What would you like to do? ').upper()
        if validate.is_valid_choice(choice):
            return choice
        else:
            print('Sorry, that was an unexpected response. Try again.\n')

def response(return_string): #print message from validate or viewmodel
    print(return_string)
