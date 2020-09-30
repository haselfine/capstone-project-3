import viewmodel as vm
import validate

def get_menu_choice(menu):
    while True:
        print(menu)
        choice = input('What would you like to do? ').upper()
        if validate.is_valid_choice(choice):
            return choice
        else:
            print('Sorry, that was an unexpected response. Try again.\n')

def response(return_string):
    print(return_string)

def array_response(return_array):
    for item in return_array:
        print(item)
