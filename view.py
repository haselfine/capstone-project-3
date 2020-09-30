from viewmodel import ViewModel as vm

def get_choice(menu):
    while True:
        print(menu)
        choice = input('What would you like to do? ')
        if menu.isvalid(choice):
            return choice
        else:
            print('Sorry, that was an unexpected response. Please enter one of the available options by its digit.')

def response(return_string):
    print(return_string)

def array_response(return_array):
    for item in return_array:
        print(item)
