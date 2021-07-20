# Starting menue
START = {'1': 'Login', '2': 'Sign Up', '3': 'Close'}  
# User abilities
USER_NAV = {'1': 'Search Movie', '2': 'View your lists', '3': 'View your watches', '4': 'Charge wallet', '5': 'Edit password', '6': 'Special Users', '7': 'Exit'}
USER_SEARCH_NAV = {'1': 'Next', '2': 'Prev', '3': 'Select', '4': 'Back'}
USER_MOVIE_NAV = {'1': 'Next', '2': 'Prev', '3': 'Watch', '4': 'Comment', '5': 'Add to list', '6': 'Close'}
USER_LIST_NAV = {'1': 'Select', '2': 'New', '3': 'Back'}
IN_LIST_NAV = {'1': 'Select', '2': 'Add current movie', '3': 'Remove movie', '4': 'Delete list', '5': 'Close'}
CHARGE_WALLET = {'1': 'Pay', '2': 'Cancel'}
EDIT_PROFILE = {'1': 'Password', '2': 'Phone Number', '3': 'Email', '4': 'Close'}
# Admin abilities
ADMIN = {'1': 'Users', '2': 'Movies', '3': 'Tags', '4': 'Exit'}
ADMIN_USER_NAV = {'1': 'Next', '2': 'Prev' ,'3': 'Back'}
ADMIN_MOVIE_NAV = {'1': 'Next', '2': 'Prev' , '3': 'Select', '4': 'New Movie', '5': 'Back'}
ADMIN_SELECT_MOVIE = {'1': 'Edit', '2': 'Delete', '3': 'Mark Special', '4': 'Close'}
ADMIN_SELECT_MOVIE_SPECIAL = {'1': 'Edit', '2': 'Delete', '3': 'Remove From Special', '4': 'Close'}
ADMIN_TAG_NAV = {'1': 'Insert', '2': 'Remove', '3': 'Back'}

def show_menu(dic):
    print()
    for key in dic.keys():
        print(f'{key}. {dic[key]}')
    print()