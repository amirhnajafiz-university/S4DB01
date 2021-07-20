# Starting menue
START = {'1': 'Login', '2': 'Sign Up', '3': 'Close'}  
# User abilities
USER = {'1': 'Search Movie', '2': 'Search List', '3': 'View your lists', '4': 'View your watches', '5': 'Charge Wallet', '6': 'Edit Profile', '7': 'Exit'}
MOVIE = {'1': 'Search by name', '2': 'Search by tag', '3': 'Back'}
SEARCH_MOVIE = {'1': 'Select', '2': 'Next', '3': 'Prev', '4': 'Back'}
SELECT_MOVIE = {'1': 'Watch', '2': 'Comment', '3': 'Add to list', '4': 'Next', '5': 'Prev', '6': 'Close'}
SEARCH_LIST = {'1': 'Select', '2': 'Back'}
SELECT_LIST = {'1': 'Select', '2': 'Back'}
SELECT_WATCH = {'1': 'Select', '2': 'Back'}
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
    for key in dic.keys():
        print(f'{key}. {dic[key]}')
    print()