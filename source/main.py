from sqlite3 import Error
from createDB import create_connection, create_database, initialize_tables
from queries import INSERT_QUERIES, DELETE_QUERIES, UPDATE_QUERIES, REQUEST_QUERIES
from import_data import load_data
from console import *
import uuid


DEF_DIR = './database/'
DATABASE = DEF_DIR + 'stream.db'
USERNAME = None

INPUT_ERROR = "Wrong input!"
VIEW_LIMIT = 5

dml_queries = {
    "insert_admin": {'list': INSERT_QUERIES, 'params': {'username': None, 'password': None}},
    "insert_comment": {'list': INSERT_QUERIES, 'params': {'rate': 0, 'user_comment': None, 'username': None, 'movie_id': None}},
    "insert_creator": {'list': INSERT_QUERIES, 'params': {'creator': None, 'movie_id': None}},
    "insert_list": {'list': INSERT_QUERIES, 'params': {'list_id': 0,'username': None, 'name': None, 'description': None}},
    "insert_movie_in_list": {'list': INSERT_QUERIES, 'params': {'special_id': 0, 'movie_id': 0, 'list_id': 0}},
    "insert_movie_tag": {'list': INSERT_QUERIES, 'params': {'tag_id': None, 'movie_id': None}},
    "insert_movie": {'list': INSERT_QUERIES, 'params': {'movie_id': None, 'movie_file': None, 'name': None, 'movie_year': None, 'description': None}},
    "insert_special_movie": {'list': INSERT_QUERIES, 'params': {'special_id': None, 'movie_id': None, 'price': None}},
    "insert_special_user": {'list': INSERT_QUERIES, 'params': {'pro_id': 0, 'username': None, 'expiredate': None}},
    "insert_tag": {'list': INSERT_QUERIES, 'params': {'tag_id': None, 'name': None}},
    "insert_user": {'list': INSERT_QUERIES, 'params': {'username': None, 'password': None, 'name': None, 'email': None, 'phonenumber': None, 'nationalID': None, 'wallet': 0, 'point': 0, 'reference': None}},
    "insert_watch_special": {'list': INSERT_QUERIES, 'params': {'pro_id': None, 'movie_id': None}},
    "insert_watch": {'list': INSERT_QUERIES, 'params': {'username': None, 'movie_id': None}},
    "clear_tables": {'list': DELETE_QUERIES, 'params': {}},
    "delete_tables": {'list': DELETE_QUERIES, 'params': {}},
    "change_movie": {'list': UPDATE_QUERIES, 'params': {'file': None, 'name': None, 'movie_year': None, 'description': None, 'movie_id': None}},
    "change_password": {'list': UPDATE_QUERIES, 'params': {'password': None, 'username': None}},
    "modify_point": {'list': UPDATE_QUERIES, 'params': {'point': 0, 'username': None}},
    "modify_wallet": {'list': UPDATE_QUERIES, 'params': {'wallet': 0, 'username': None}},
    "remove_user_pro": {'list': UPDATE_QUERIES, 'params': {'pro_id': None}},
    "remove_movie_from_list": {'list': UPDATE_QUERIES, 'params': {'movie_id': 0, 'list_id': 0}},
    "remove_movie": {'list': UPDATE_QUERIES, 'params': {'movie_id': 0}},
    "remove_user": {'list': UPDATE_QUERIES, 'params': {'username': None}},
    "remove_special_movie": {'list': UPDATE_QUERIES, 'params': {'movie_id': None}},
    "remove_tag": {'list': UPDATE_QUERIES, 'params': {'tag_id': 0}},
    "get_comments": {'list': REQUEST_QUERIES, 'params': {'movie_id': 0}},
    "get_list": {'list': REQUEST_QUERIES, 'params': {'username': None}},
    "get_movie_by_tag": {'list': REQUEST_QUERIES, 'params': {'tag': None}},
    "get_movie_creators": {'list': REQUEST_QUERIES, 'params': {'movie_id': 0}},
    "get_movies_of_list": {'list': REQUEST_QUERIES, 'params': {'list_id': 0}},
    "get_tags": {'list': REQUEST_QUERIES, 'params': {}},
    "admin_login": {'list': REQUEST_QUERIES, 'params': {'username': None, 'password': None}},
    "get_movies": {'list': REQUEST_QUERIES, 'params': {'offset': 0}},
    "get_users": {'list': REQUEST_QUERIES, 'params': {'offset': 0}},
    "special_movie": {'list': REQUEST_QUERIES, 'params': {'movie_id': 0}},
    "special_user": {'list': REQUEST_QUERIES, 'params': {'username': None}},
    "user_login": {'list': REQUEST_QUERIES, 'params': {'username': None, 'password': None}},
    "user_point": {'list': REQUEST_QUERIES, 'params': {'username': None}},
    "user_wallet": {'list': REQUEST_QUERIES, 'params': {'username': None}},
    "user_watch_special": {'list': REQUEST_QUERIES, 'params': {'pro_id': None}},
    "user_watch": {'list': REQUEST_QUERIES, 'params': {'username': None}},
    "get_number_of_users": {'list': REQUEST_QUERIES, 'params': {}},
    "get_number_of_movies": {'list': REQUEST_QUERIES, 'params': {}},
    "get_movie_tags": {'list': REQUEST_QUERIES, 'params': {'movie_id': None}},
    "is_special_movie": {'list': REQUEST_QUERIES, 'params': {'movie_id': None}},
}


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
        c.executescript(DELETE_QUERIES[query])
    except Error as e:
        print(e)
        connection.rollback()


def execute_query(connection, query, inputs):
    """
    This method executes a query that is insert or update.
    """
    try:
        c = connection.cursor()
        c.execute("BEGIN TRANSACTION;")
        c.execute(dml_queries[query]['list'][query], inputs)
        c.execute("COMMIT;")
        print("> Commited")
        return True
    except Error as e:
        print(e)
        c.execute("ROLLBACK")
        return False


def execute_get_query(connection, query, inputs):
    """
    This method executes type of queries that return a data from database.
    """
    data = None
    try:
        c = connection.cursor()
        c.execute(dml_queries[query]['list'][query], list(inputs))
        data = c.fetchall()
    except Error as e:
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


def printData(data):
    index = 1
    for item in data:
        print(f"{index}. {item}")
        index += 1


def view_users_panel(connection):
    "This method shows all the users to admin"
    offset = 0
    total = execute_get_query(connection=connection, query="get_number_of_users", inputs=[])[0][0]
    while True:
        print(f"Total found: {total}")
        data = execute_get_query(connection=connection, query="get_users", inputs=[offset])
        printData(data=data)
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
    print("If you don't want to give non require fields a value, just press enter.")
    id = str(uuid.uuid1().int)
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
    if execute_query(connection=connection, query="insert_movie", inputs=[id, file, name, year, description]):
        if tags:
            for tag in tags:
                execute_query(connection=connection, query="insert_movie_tag", inputs=[data[int(tag)][0], id])
        for creator in creators:
            execute_query(connection=connection, query="insert_creator", inputs=[creator, id])
        if flag:
            execute_query(connection=connection, query="insert_special_movie", inputs=[int(str(uuid.uuid1().int)[-16:]), id, price])


def view_movie(connection, data):
    flag = execute_get_query(connection=connection, query="is_special_movie", inputs=[data[0]])
    creators = execute_get_query(connection=connection, query="get_movie_creators", inputs=[data[0]])
    tags = execute_get_query(connection=connection, query="get_movie_tags", inputs=[data[0]])
    while True:
        print(data)
        if creators:
            print("Movie creator:")
            printData(creators[0])
        if tags:
            print("Movie tags:")
            printData(tags[0])
        if flag:
            print("* Special Movie")
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
    offset = 0
    total = execute_get_query(connection=connection, query="get_number_of_movies", inputs=[])[0][0]
    while True:
        print(f"Total found: {total}")
        data = execute_get_query(connection=connection, query="get_movies", inputs=[offset])
        printData(data=data)
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
    while True:
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
    # todo: Admin can: add movie, remove movie, add a tag, remove a tag, change a tag, add special movie, remove special movie, edit movie, view users, view movies, view lists
    while True:
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


def user_panel(connection):
    pass # todo: User can: watch movie, increase wallet, comment, make list, add to list, remove from list, view movies, view lists, and go pro


def login(connection):
    """
    Login panel where the user enters username and password and we check the information.
    """
    data = {}
    data['username'] = "amirhossein" # input("> Enter Username: ")
    data['password'] = "1270" # input("> Enter Password: ")
    result = execute_get_query(connection=connection, query='admin_login', inputs=data.values())
    if result:
        USERNAME = result[0][0]
        admin_panel(connection=connection)
    result = execute_get_query(connection=connection, query='user_login', inputs=data.values())
    if result:
        USERNAME = result[0][0]
        user_panel(connection=connection)
    print("Login faild.")


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
    connection = create_connection(DATABASE)
    while True:
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