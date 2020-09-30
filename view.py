from viewmodel import ViewModel as vm

def user_input(menu):
    print(menu)
    choice = input('What would you like to do? ')
    if menu.isvalid(choice):
        return choice
    else:
        print('Sorry, that was an unexpected response. Please enter one of the available options by its digit.')

def response(return_data):
    print(return_data)

def 