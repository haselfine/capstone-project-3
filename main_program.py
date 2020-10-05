from menu import Menu
import view
import viewmodel as vm
import validate

'''
See README.md
'''

def main():
    menu = create_menu() #just numbers and descriptions

    while True: #continue until q
        user_choice = view.get_menu_choice(menu)
        if user_choice.upper() == 'Q':
            break
        valid_response = menu_actions(user_choice)
        view.response(valid_response + '\n')

def create_menu():
    menu = Menu()
    menu.add_option('1', "Add artist")
    menu.add_option('2', "Add artwork")
    menu.add_option('3', "Get all artwork (available & unavailable)")
    menu.add_option('4', "Get all available artwork")
    menu.add_option('5', "Delete an artwork")
    menu.add_option('6', "Update artwork availability")
    menu.add_option('Q', "Quit")
    return menu

def menu_actions(user_choice):
    if user_choice == '1':
        return add_artist()
    elif user_choice == '2':
        return add_artwork()
    elif user_choice == '3':
        return get_all_artwork()
    elif user_choice == '4':
        return get_all_available_artwork()
    elif user_choice == '5':
        return delete_artwork()
    elif user_choice == '6':
        return update_artwork()

def add_artist(): 
    artist_info = validate.validate_artist() #returns a list of [0]: success/failure and if successful [1]: artist name, [2]: artist email
    if artist_info[0] == 'artist-success':
        return vm.add_artist(artist_info[1], artist_info[2]) #send to viewmodel to send to database
    else:
        return artist_info[0] #error message

def add_artwork():
    artwork_info = validate.validate_artwork() #returns same as add_artist except [1]: artist id, [2]: artwork name, [3]: price, [4]: availability
    if artwork_info[0] == 'artwork-success':
        return vm.add_artwork(artwork_info[1], str(artwork_info[2]), artwork_info[3], artwork_info[4])
    else:
        return artwork_info[0]

def get_all_artwork():
    db_validity_and_artist = validate.validate_artist_db() #returns [0]: success/failure (True vs. False), [1]: query object
    if db_validity_and_artist[0]:
        all_artwork_list = listify_artwork(vm.get_all_artwork(db_validity_and_artist[1])) #convert query object to list of strings
        if len(all_artwork_list) > 0: #if it isn't empty, convert list into single string
            return stringify_artwork(all_artwork_list)
        else: 
            return 'No artwork by that artist'
    
def get_all_available_artwork():
    db_validity_and_artist = validate.validate_artist_db() #almost exactly the same as get_all except uses viewmodel's get_all_available function instead
    if db_validity_and_artist[0]:
        available_artwork_list = listify_artwork(vm.get_all_available_artwork(db_validity_and_artist[1]))
        if len(available_artwork_list) > 0:
            return stringify_artwork(available_artwork_list)
        else:
            return 'No artwork by that artist'
    else:
        return 'Could not find that artist'

def delete_artwork():
    db_validity_and_artist = validate.validate_artist_db() #returns [0]: success/failure (True vs False), [1]: artist id
    if db_validity_and_artist[0]:
        db_validity_and_artwork = validate.validate_artwork_db(db_validity_and_artist[1]) #returns same as above except [1]: artwork name
        if db_validity_and_artwork[0]:
            if validate.are_you_sure('Are you sure you would like to delete the artwork'): #checks if user is certain
                vm.delete_artwork(db_validity_and_artist[1], db_validity_and_artwork[1]) #send to viewmodel to delete
                return f'{db_validity_and_artwork[1]} was deleted.'
            else:
                return 'Artwork was not deleted.'
        else:
            return f'Could not find artwork named "{db_validity_and_artwork[1]}" by {db_validity_and_artwork[1]}.'
    else:
        return f'Could not find artist {db_validity_and_artist[1]}.'

def update_artwork(): #almost the same as delete except sends to update function in viewmodel
    db_validity_and_artist = validate.validate_artist_db()
    if db_validity_and_artist[0]:
        db_validity_and_artwork = validate.validate_artwork_db(db_validity_and_artist[1])
        if db_validity_and_artwork[0]:
            if validate.are_you_sure('Is the artwork available') == True:
                vm.update_artwork(db_validity_and_artist[1], db_validity_and_artwork[1], 1)
                return f'{db_validity_and_artwork[1]} was updated to "Available"'
            else:
                vm.update_artwork(db_validity_and_artist[1], db_validity_and_artwork[1], 0)
                return f'{db_validity_and_artwork[1]} was updated to "Unavailable"'
        else:
            return f'Could not find artwork named "{db_validity_and_artwork[1]}" by {db_validity_and_artwork[1]}.'
    else:
        return f'Could not find artist {db_validity_and_artist[1]}.'

def listify_artwork(artwork_obj):
    artwork_list = []
    for artwork in artwork_obj:
        if artwork is not None:
            artwork_string = f'Name: {artwork.artwork_name} | Price: {artwork.price} | Available? {artwork.available}' #turn each result into a user friendly string
            artwork_list.append(artwork_string)
    return artwork_list

def stringify_artwork(artwork_list):
    return '\n'.join(artwork_list) #turn into a single string

if __name__ == '__main__':
    main()