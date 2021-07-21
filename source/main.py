from sqlite3 import Error
from createDB import create_connection, create_database, initialize_tables
from queries import QUERIES
from import_data import load_data
from console import *
import uuid
import os
import datetime
from dateutil import parser
import math


DEF_DIR = './database/'
DATABASE = DEF_DIR + 'stream.db'
USERNAME = None
ISADMIN = False
PRO_ID = None
USER_DATA = None

ERROR_MESSAGE = None
ERROR = False

INPUT_ERROR = "Wrong input!"
VIEW_LIMIT = 5
SPLITTER = "==============================="


def init():
    """
    By running this method, we create our database and tables.

    """
    create_database(db_file=DATABASE)
    connection = create_connection(db_file=DATABASE)
    initialize_tables(connection=connection)
    connection.close()


def execute_delete(connection, query):
    """
    This method executes the queries that we give for deleting functions.
    """
    try:
        c = connection.cursor()
        c.executescript(QUERIES[query])
    except Error as e:
        print(e)
        connection.rollback()


def reset(connection):
    """
    This method resets the database.
    """
    execute_delete(connection=connection, query="delete_tables")


def execute_query(connection, query, inputs, allow_commit=True, disable_transation=False):
    """
    This method executes a query that is insert or update.
    """
    global ERROR_MESSAGE, ERROR
    try:
        c = connection.cursor()
        if not disable_transation:
            c.execute("BEGIN TRANSACTION;")
        c.execute(QUERIES[query], inputs)
        if allow_commit:
            c.execute("COMMIT;")
            print("> Commited")
        ERROR = False
        return True
    except Error as e:
        ERROR_MESSAGE = e
        ERROR = True
        print(e)
        c.execute("ROLLBACK")
        return False


def execute_get_query(connection, query, inputs):
    """
    This method executes type of queries that return a data from database.
    """
    global ERROR, ERROR_MESSAGE
    data = None
    try:
        c = connection.cursor()
        c.execute(QUERIES[query], list(inputs))
        data = c.fetchall()
        ERROR = False
    except Error as e:
        ERROR_MESSAGE = e
        ERROR = True
        print(e)
    finally:
        return data


def import_temp_data(connection):
    """
    This method imports a template data to our database
    """
    data = load_data()
    for obj in data.values():
        execute_query(connection=connection, query=obj['op'], inputs=list(obj['data'].values()))


def clearScreen():
    """
    Simple method for formatting the console.
    """
    # os.system('cls' if os.name=='nt' else 'clear')
    if ISADMIN:
        print(f"User {USERNAME} ", end="")
        print("As Admin\n")
    else:
        print(f"User: {USER_DATA[2]} | Mail: {USER_DATA[3]} | Phone: {USER_DATA[4]} | Points: {USER_DATA[7]}", end="")
        if PRO_ID:
            print(" | You are a pro user.")
        else:
            print()
    print(SPLITTER)


def printData(data, primary_key_hide=True):
    """
    This method gets a list and prints it.
    """
    if len(data) > 0:
        print(SPLITTER)
    index = 1
    for item in data:
        print(f"{index}.", end=" ")
        for i in range(len(item)):
            if i == 0 and primary_key_hide:
                continue
            print(f"{item[i]}", end="")
            if i == len(item) - 1:
                print()
            else:
                print(" | ", end="")
        index += 1
    if len(data) > 0:
        print(SPLITTER)


def calculate_page(offset, total):
    """
    This method simply gets the status of paging for us.
    """
    pages = math.ceil(total / VIEW_LIMIT)
    current = math.ceil(offset / VIEW_LIMIT)
    if current == 0 and pages != 0:
        current = 1
    return (current, pages)


def printMovies(connection, data):
    """
    This method print the movies.
    """
    index = 1
    if len(data) > 0:
        print(SPLITTER)
    for item in data:
        print(f"{index}.", end=" ")
        for i in range(len(item)):
            if i == 0:
                continue
            print(f"{item[i]}", end="")
            if i != len(item) - 1:
                print(" | ", end="")          
        if execute_get_query(connection=connection, query="is_special_movie", inputs=[item[0]]):
            print(" => Special\n")
        else:
            print("\n")
        index += 1
    if len(data) > 0:
        print(SPLITTER)


def view_users_panel(connection):
    """
    This method is the user viewing panel, for admin to check users.
    """
    offset = 0  # Creating an offset so the admin can view the data
    while True:
        clearScreen()
        total = execute_get_query(connection=connection, query="get_number_of_users", inputs=[])[0][0]  # Total number of records
        print(f"Total found: {total}")
        data = execute_get_query(connection=connection, query="get_users", inputs=[offset])
        printData(data=data, primary_key_hide=False)
        status = calculate_page(offset=offset, total=total)
        print(f"\nPage {status[0]} of {status[1]}\n")
        show_menu(ADMIN_USER_NAV)
        command = input("> ")
        if command == "1":
            if offset + VIEW_LIMIT < total:
                offset += VIEW_LIMIT
        elif command == "2":
            if offset - VIEW_LIMIT >= 0:
                offset -= VIEW_LIMIT
        elif command == "3":
            break
        else:
            print(INPUT_ERROR)


def edit_movie(connection, data):
    """
    This method runs the functionality of editing a movie.
    """
    print("If you don't want to change a field, just press enter.")
    file = input("Movie file > ")
    if file == "":
        file = data[1]
    name = input("Movie name > ")
    if name == "":
        name = data[2]
    year = input("Movie year > ")
    if year == "":
        year = data[3]
    description = input("Movie description > ")
    if description == "":
        description = data[4]
    execute_query(connection=connection, query="change_movie", inputs=[file, name, year, description, data[0]])


def add_movie(connection):
    """
    This method runs the functionality of inserting a new movie.
    """
    print("If you don't want to give non require fields a value, just press enter.")
    id = str(uuid.uuid1().int)  # Generate an id for the movie
    file = input("Movie file * > ")
    if file == "":
        while file != "":
            file = input("Movie file * > ")
    name = input("Movie name * > ")
    if name == "":
        while name != "":
            name = input("Movie name * > ")
    year = int(input("Movie year * > "))
    if year == "":
        while year != "":
            year = input("Movie year * > ")
    description = input("Movie description > ")
    if description == "":
        description = None
    print("Choose the tags you want for this movie: ")
    data = execute_get_query(connection=connection, query="get_tags", inputs=[])
    tags = None
    if data:
        print("Tags: ")
        printData(data=data)
        tags = input("Enter tags index like 1,2,... > ")
        if tags == "":
            tags = []
        else:
            tags = tags.split(",")
    print("Enter the movie creators: ")
    creators = input("Enter like Adam,Martix,..... > ")
    if creators == "":
        creators = []
    else:
        creators = creators.split(",")
    flag = input("Do you want this to be special movie ?(Y/n)> ")
    price = 0
    if flag == "Y":
        price = int(input("Enter price > "))
    code = []
    try:  # Starting transaction
        if execute_query(connection=connection, query="insert_movie", inputs=[id, file, name, year, description], allow_commit=False):
            if tags:
                for tag in tags:
                    code.append(execute_query(connection=connection, query="insert_movie_tag", inputs=[data[int(tag)-1][0], id], allow_commit=False, disable_transation=True))
            for creator in creators:
                code.append(execute_query(connection=connection, query="insert_creator", inputs=[creator, id], allow_commit=False, disable_transation=True))
            if flag == "Y":
                code.append(execute_query(connection=connection, query="insert_special_movie", inputs=[int(str(uuid.uuid1().int)[-16:]), id, price], allow_commit=False, disable_transation=True))
            for single in code:
                if not single:
                    connection.rollback()
                    print("Rollback")
                    return
            connection.commit()
    except Exception as e:
        print(e)
        connection.rollback()


def view_movie(connection, data):
    """
    This method sends the admin to a single movie viewing.
    """
    flag = execute_get_query(connection=connection, query="is_special_movie", inputs=[data[0]])
    creators = execute_get_query(connection=connection, query="get_movie_creators", inputs=[data[0]])
    tags = execute_get_query(connection=connection, query="get_movie_tags", inputs=[data[0]])
    while True:
        clearScreen()
        print(data)
        if creators:
            print("Movie creator:")
            printData(creators[0])
        if tags:
            print("Movie tags:")
            printData(tags[0])
        if flag:
            print(f'Price: {flag[0][2]}$')
            show_menu(ADMIN_SELECT_MOVIE_SPECIAL)
        else:
            show_menu(ADMIN_SELECT_MOVIE)
        command = input("> ")
        if command == "1":
            edit_movie(connection=connection, data=data)
            break
        elif command == "2":
            execute_query(connection=connection, query="remove_movie", inputs=[data[0]])
            break
        elif command == "3":
            if flag:
                execute_query(connection=connection, query="remove_special_movie", inputs=[data[0]])
            else:
                price = int(input("Enter the price > "))
                execute_query(connection=connection, query="insert_special_movie", inputs=[int(str(uuid.uuid1().int)[-16:]), data[0], price])
            break
        elif command == "4":
            break
        else:
            print(INPUT_ERROR)


def view_movies_panel(connection):
    """
    This method generates the view port of movies for admin to navigate.
    """
    offset = 0
    while True:
        clearScreen()
        total = execute_get_query(connection=connection, query="get_number_of_movies", inputs=[])[0][0]
        print(f"Total found: {total}")
        data = execute_get_query(connection=connection, query="get_movies", inputs=[offset])
        printMovies(connection=connection, data=data)
        status = calculate_page(offset=offset, total=total)
        print(f"\nPage {status[0]} of {status[1]}\n")
        show_menu(ADMIN_MOVIE_NAV)
        command = input("> ")
        if command == "1":
            if offset + VIEW_LIMIT < total:
                offset += VIEW_LIMIT
        elif command == "2":
            if offset - VIEW_LIMIT >= 0:
                offset -= VIEW_LIMIT
        elif command == "3":
            code = int(input("Which one ?> "))
            view_movie(connection, data[code-1])
        elif command == "4":
            add_movie(connection=connection)
        elif command == "5":
            break
        else:
            print(INPUT_ERROR)


def view_tags(connection):
    """
    This method generates the view of tag modifying panel for admin.
    """
    while True:
        clearScreen()
        data = execute_get_query(connection=connection, query="get_tags", inputs=[])
        if data:
            data = data
            print("Tags:")
            printData(data)
        else:
            print("No tags.")
        show_menu(ADMIN_TAG_NAV)
        command = input("> ")
        if command == "1":
            name = input("Name > ")
            execute_query(connection=connection, query="insert_tag", inputs=[int(str(uuid.uuid1().int)[-16:]), name])
        elif command == "2":
            if data:
                index = int(input("Which one ?> "))
                execute_query(connection=connection, query="remove_tag", inputs=[data[index-1][0]])
        elif command == "3":
            break
        else:
            print(INPUT_ERROR)


def admin_panel(connection):
    """
    Admin panel routes the admin to different parts of the admin panel.
    """
    while True:
        clearScreen()
        show_menu(ADMIN)
        command = input("> ")
        if command == '1':
            view_users_panel(connection=connection)
        elif command == '2':
            view_movies_panel(connection=connection)
        elif command == '3':
            view_tags(connection=connection)
        elif command == '4':
            break
        else:
            print(INPUT_ERROR)


def search_by_tag(connection, tags, choosed_tags, pattern, offset):
    """
    This method search among the movies by tags we give.
    """
    total = 0
    data = []
    for tag in choosed_tags:
        garb = execute_get_query(connection=connection, query="get_number_of_search_movie_by_tag", inputs=[tags[int(tag)-1][1], f"%{pattern}%"])
        if garb:
            total += garb[0][0]
        temp = execute_get_query(connection=connection, query="get_movie_by_tag", inputs=[tags[int(tag)-1][1], f"%{pattern}%", offset])
        if temp:
            data = data + temp
    return (list(dict.fromkeys(data)), total)


def watch_movie(connection, movie_id, is_special):
    """
    This method inserts a new watch for user.
    """
    if is_special:
        if PRO_ID == None:
            if execute_query(connection=connection, query="modify_point", inputs=[-1, USERNAME], allow_commit=False):
                if execute_query(connection=connection, query="insert_watch", inputs=[USERNAME, movie_id], disable_transation=True):
                    connection.commit()
                else:
                    connection.rollback()
        else:
            execute_query(connection=connection, query="insert_watch_special", inputs=[PRO_ID, movie_id])
    else:
        execute_query(connection=connection, query="insert_watch", inputs=[USERNAME, movie_id])


def comment_this_movie(connection, movie_id):
    """
    This method comments a user opinion for a movie.
    """
    rate = int(input("Enter a rate between 0 to 5 > "))
    comment = input("Enter your comment > ")
    execute_query(connection=connection, query="insert_comment", inputs=[rate, comment, USERNAME, movie_id])


def select_this_movie(connection, data):
    """
    This method selects a movie for our user.
    """
    flag = execute_get_query(connection=connection, query="is_special_movie", inputs=[data[0]])
    creators = execute_get_query(connection=connection, query="get_movie_creators", inputs=[data[0]])
    tags = execute_get_query(connection=connection, query="get_movie_tags", inputs=[data[0]])
    offset = 0
    while True:
        total = execute_get_query(connection=connection, query="get_number_of_comments", inputs=[data[0]])
        average = execute_get_query(connection=connection, query="get_average_rate", inputs=[data[0]])
        if total:
            total = total[0][0]
        else:
            total = 0
        comments = execute_get_query(connection=connection, query="get_comments", inputs=[data[0], offset])
        clearScreen()
        printMovies(connection=connection, data=[data])
        if creators:
            print("Movie creator:")
            printData(creators)
        if tags:
            print("Movie tags:")
            printData(tags)
        if flag:
            print(f'Price: {flag[0][2]}$')
        print(f"\nAverage rate by users {average[0][0]}.\n")
        if comments:
            print("Movie Comments:")
            printData(comments)
        show_menu(USER_MOVIE_NAV)
        status = calculate_page(offset=offset, total=total)
        print(f"\nPage {status[0]} of {status[1]}\n")
        command = input("> ")
        if command == "1":
            if offset + VIEW_LIMIT < total:
                offset += VIEW_LIMIT
        elif command == "2":
            if offset - VIEW_LIMIT >= 0:
                offset -= VIEW_LIMIT
        elif command == "3":
            if flag and PRO_ID == None:
                temp = input("Since this is special movie you will loose 1 point to see this, do you want ?(Y/n)> ")
                if temp == "Y":
                    watch_movie(connection=connection, movie_id=data[0], is_special=flag)
            else:
                watch_movie(connection=connection, movie_id=data[0], is_special=flag)
        elif command == "4":
            comment_this_movie(connection=connection, movie_id=data[0])
        elif command == "5":
            user_list_panel(connection=connection, movie_id=data[0])
        elif command == "6":
            break
        else:
            print(INPUT_ERROR)


def user_search_panel(connection):
    """
    User search panel lets the user to search in movies
    """
    clearScreen()
    key = input("Enter a name, or a part of name for search > ")
    if key == "":
        key = "_"
    tags = execute_get_query(connection=connection, query="get_tags", inputs=[])
    allow_tags = input("Do you want to search based on special tags ?(Y/n)> ")
    choosed_tags = []
    if allow_tags == "Y":
        if tags:
            print("Tags:")
            printData(tags)
        else:
            print("No tags avilable.")
    if tags and allow_tags == "Y":
        choosed_tags = input("Enter them like 1,2,... > ")
        choosed_tags = choosed_tags.split(",")
    offset = 0
    total = 0
    while True:
        clearScreen()
        data = []
        if tags and allow_tags == "Y":
            result = search_by_tag(connection=connection, tags=tags, choosed_tags=choosed_tags, pattern=key, offset=offset)
            data = result[0]
            total = result[1]
        else:
            data = execute_get_query(connection=connection, query="search_movie", inputs=[f"%{key}%", offset])
            total = execute_get_query(connection=connection, query="get_number_of_search_movie", inputs=[f"%{key}%"])
            if total:
                total = total[0][0]
            else: 
                total = 0
        printMovies(connection=connection, data=data)
        status = calculate_page(offset=offset, total=total)
        print(f"\nPage {status[0]} of {status[1]}\n")
        show_menu(USER_SEARCH_NAV)
        command = input("> ")
        if command == "1":
            if offset + VIEW_LIMIT < total:
                offset += VIEW_LIMIT
        elif command == "2":
            if offset - VIEW_LIMIT >= 0:
                offset -= VIEW_LIMIT
        elif command == "3":
            index = input("Which one ?> ")
            select_this_movie(connection=connection, data=data[int(index)-1])
        elif command == "4":
            break
        else:
            print(INPUT_ERROR)


def user_watch_panel(connection):
    """
    This method shows the user the history of the user movies.
    """
    data = execute_get_query(connection=connection, query="user_watch", inputs=[USERNAME])
    special_data = None
    if PRO_ID:
        special_data = execute_get_query(connection=connection, query="user_watch_special", inputs=[PRO_ID])
    if data:
        print("Your history:")
        printData(data=data)
    if special_data:
        print("Special movies:")
        printData(data=special_data)
    input("Press enter to exit > ")


def new_list(connection):
    """
    This method inserts a new list for a user.
    """
    id = int(str(uuid.uuid1().int)[-16:])
    name = input("Enter name *> ")
    if name == "":
        while name != "":
            name = input("Enter name *> ")
    description = input("Description > ")
    execute_query(connection=connection, query="insert_list", inputs=[id, USERNAME, name, description])


def add_movie_to_list(connection, movie_id, list_id):
    """
    Add a specific movie to user list.
    """
    execute_query(connection=connection, query="insert_movie_in_list", inputs=[movie_id, list_id])


def remove_list(connection, list_id):
    """
    Remove a full list.
    """
    execute_query(connection=connection, query="remove_list", inputs=[list_id])

def remove_movie_from_list(connection, list_id, movie_id):
    """
    Remove a single movie from a list.
    """
    execute_query(connection=connection, query="remove_movie_from_list", inputs=[movie_id, list_id])


def view_list(connection, data, movie_id=None):
    """
    View list is the method to send the user into the list view panel.
    """
    while True:
        clearScreen()
        movies = execute_get_query(connection=connection, query="get_movies_of_list", inputs=[data[0]])
        if movies:
            print("Movies:")
            printMovies(connection=connection, data=movies)
        else:
            print("No movies yet!")
        show_menu(IN_LIST_NAV)
        command = input("> ")
        if command == "1":
            index = input("Which one ?> ")
            select_this_movie(connection=connection, data=movies[int(index)-1])
        elif command == "2":
            if movie_id:
                add_movie_to_list(connection=connection, movie_id=movie_id, list_id=data[0])
            else:
                print("No movies selected.")
        elif command == "3":
            index = input("Which one ?> ")
            remove_movie_from_list(connection=connection, list_id=data[0], movie_id=movies[int(index)-1][0])
        elif command == "4":
            remove_list(connection=connection, list_id=data[0])
            break
        elif command == "5":
            break
        else:
            print(INPUT_ERROR)


def user_list_panel(connection, movie_id=None):
    """
    User list panel is the panel that shows the user lists and their content.
    """
    while True:
        clearScreen()
        data = execute_get_query(connection=connection, query="get_list", inputs=[USERNAME])
        if data:
            print("Current lists:")
            printData(data=data)
        else:
            print("No lists yet!")
        show_menu(USER_LIST_NAV)
        command = input("> ")
        if command == "1":
            index = input("Which one ?> ")
            view_list(connection=connection, data=data[int(index)-1], movie_id=movie_id)
        elif command == "2":
            new_list(connection=connection)
        elif command == "3":
            break
        else:
            print(INPUT_ERROR)


def pay_money(connection, amount):
    """
    This method allows the user to charge its account.
    """
    execute_query(connection=connection, query="modify_wallet", inputs=[amount, USERNAME])


def user_pay_panel(connection):
    """
    This method views the user wallet panel.
    """
    while True:
        clearScreen()
        current = execute_get_query(connection=connection, query="user_wallet", inputs=[USERNAME])
        print(f"Your current wallet is  {current[0][0]} $")
        show_menu(CHARGE_WALLET)
        command = input("> ")
        if command == "1":
            amount = input("How mush ?> ")
            pay_money(connection=connection, amount=amount)
        elif command == "2":
            break
        else:
            print(INPUT_ERROR)


def password_change(connection):
    """
    This method allows the user to change its password.
    """
    while True:
        password = input("Enter the new password > ")
        if execute_query(connection=connection, query="change_password", inputs=[password, USERNAME]):
            break


def profile_change(connection):
    """
    This method changes the profile of the user.
    """
    global USER_DATA
    while True:
        USER_DATA = execute_get_query(connection=connection, query="get_user", inputs=[USERNAME])
        if USER_DATA:
            USER_DATA = USER_DATA[0]
        clearScreen()
        show_menu(USER_PROFILE_CHANGE)
        command = input("> ")
        if command == "1":
            name = input("New name > ")
            execute_query(connection=connection, query="change_name", inputs=[name, USERNAME])
        elif command == "2":
            email = input("New mail > ")
            execute_query(connection=connection, query="change_email", inputs=[email, USERNAME])
        elif command == "3":
            phone = input("New phone number > ")
            execute_query(connection=connection, query="change_phone", inputs=[phone, USERNAME])
        elif command == "4":
            break
        else:
            print(INPUT_ERROR)


def add_pro_user(connection):
    """
    This method adds a new user to the pro users list.
    """
    global PRO_ID
    if execute_query(connection=connection, query="modify_wallet", inputs=[-50, USERNAME], allow_commit=False):
        id = int(str(uuid.uuid1().int)[-16:])
        ex_date = datetime.datetime.now() + datetime.timedelta(days=30)
        if execute_query(connection=connection, query="insert_special_user", inputs=[id, USERNAME, ex_date], disable_transation=True):
            PRO_ID = id
            connection.commit()
        else:
            connection.rollback()


def update_credit(connection, ex_date):
    """
    This method updates the time credit for a special user.
    """
    if execute_query(connection=connection, query="modify_wallet", inputs=[-50, USERNAME], allow_commit=False):
        new_date = parser.parse(ex_date) + datetime.timedelta(days=30)
        if execute_query(connection=connection, query="update_credit", inputs=[new_date, PRO_ID], disable_transation=True):
            connection.commit()
        else:
            connection.rollback()


def pro_panel(connection):
    """
    Pro panel represents the panel for showing the current status of pro user and updating status.
    """
    while True:
        clearScreen()
        if PRO_ID:
            ex_date = execute_get_query(connection=connection, query="get_current_credit", inputs=[PRO_ID])[0][0]
            print(f"You are a pro user until {ex_date}")
        else:
            print("You are a normal user.")
        show_menu(PRO_PANEL_NAVIGATION)
        command = input("> ")
        if command == "1":
            if not PRO_ID:
                add_pro_user(connection=connection)
            else:
                update_credit(connection=connection, ex_date=ex_date)
        elif command == "2":
            break
        else:
            print(INPUT_ERROR)


def user_panel(connection):
    """
    User panel routes the user to different parts of the user panel
    """
    while True:
        clearScreen()
        show_menu(USER_NAV)
        command = input("> ")
        if command == '1':
            user_search_panel(connection=connection)
        elif command == '2':
            user_list_panel(connection=connection)
        elif command == '3':
            user_watch_panel(connection=connection)
        elif command == '4':
            user_pay_panel(connection=connection)
        elif command == '5':
            pro_panel(connection=connection)
        elif command == '6':
            password_change(connection=connection)
        elif command == '7':
            profile_change(connection=connection)
        elif command == '8':
            break
        else:
            print(INPUT_ERROR)


def login(connection):
    """
    Login panel where the user enters username and password and we check the information.
    """
    global USERNAME, ISADMIN, PRO_ID, USER_DATA
    data = {}
    data['username'] = "user6" # input("> Enter Username: ")
    data['password'] = "p66666666" # input("> Enter Password: ")
    result = execute_get_query(connection=connection, query='admin_login', inputs=data.values())
    if result:
        USERNAME = result[0][0]
        ISADMIN = True
        admin_panel(connection=connection)
    result = execute_get_query(connection=connection, query='user_login', inputs=data.values())
    if result:
        USERNAME = result[0][0]
        flag = execute_get_query(connection=connection, query="special_user", inputs=[USERNAME])
        if flag:
            PRO_ID = flag[0][0]
        USER_DATA = result[0]
        user_panel(connection=connection)


def sign_up(connection):
    """
    Sign up panel where each new user enters its information to register.
    """
    data = {}
    data['username'] = input("> Enter Username: ")
    data['password'] = input("> Enter Password: ")
    data['name'] = input("> Enter Name: ")
    data['email'] = input("> Enter Email: ")
    data['phone'] = input("> Enter Phone Number: ")
    data['ID'] = input("> Enter National ID: ")
    data['wallet'] = 0
    data['point'] = 0
    data['reference'] = input("> If you were invited by a user enter their username, if not just press enter: ")
    if data['reference'] == '':
        data['reference'] = None
    if execute_query(connection=connection, query='insert_user', inputs=list(data.values())):
        if data['reference']:
            execute_query(connection=connection, query='modify_point', inputs=[1, data['reference']])
        print("Registerd Successfuly.")
    else:
        print("Failed Registration.")
        return


def root():
    """
    root is our project main function that starts the application.
    """
    connection = create_connection(DATABASE)
    while True:
        os.system('cls' if os.name=='nt' else 'clear')
        show_menu(START)
        command = input("> ")
        if command == '1':
            login(connection=connection)
        elif command == '2':
            sign_up(connection=connection)
        elif command == '3':
            break
        else:
            print(INPUT_ERROR)
    connection.close()


if __name__ == '__main__':
    root()
