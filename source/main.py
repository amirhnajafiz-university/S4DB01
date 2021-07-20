from sqlite3 import Error
from createDB import create_connection, create_database, initialize_tables
from queries import INSERT_QUERIES, DELETE_QUERIES, UPDATE_QUERIES, REQUEST_QUERIES
from import_data import load_data
from console import *


DEF_DIR = './database/'
DATABASE = DEF_DIR + 'stream.db'

dml_queries = {
    "insert_admin": {'list': INSERT_QUERIES, 'params': {'username': None, 'password': None}},
    "insert_comment": {'list': INSERT_QUERIES, 'params': {'rate': 0, 'user_comment': None, 'username': None, 'movie_id': None}},
    "insert_creator": {'list': INSERT_QUERIES, 'params': {'creator': None, 'movie_id': None}},
    "insert_list": {'list': INSERT_QUERIES, 'params': {'list_id': 0,'username': None, 'name': None, 'description': None}},
    "insert_movie_in_list": {'list': INSERT_QUERIES, 'params': {'special_id': 0, 'movie_id': 0, 'list_id': 0}},
    "insert_movie_tag": {'list': INSERT_QUERIES, 'params': {'tag_id': None, 'movie_id': None}},
    "insert_movie": {'list': INSERT_QUERIES, 'params': {'movie_id': None, 'movie_file': None, 'name': None, 'movie_year': None, 'description': None}},
    "insert_special_movie": {'list': INSERT_QUERIES, 'params': {'movie_id': None, 'price': None}},
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
    "get_comments": {'list': REQUEST_QUERIES, 'params': {'movie_id': 0}},
    "get_list": {'list': REQUEST_QUERIES, 'params': {'username': None}},
    "get_movie_by_tag": {'list': REQUEST_QUERIES, 'params': {'tag': None}},
    "get_movie_creators": {'list': REQUEST_QUERIES, 'params': {'movie_id': 0}},
    "get_movies_of_list": {'list': REQUEST_QUERIES, 'params': {'list_id': 0}},
    "get_tags": {'list': REQUEST_QUERIES, 'params': {'name': None}},
    "search_admin": {'list': REQUEST_QUERIES, 'params': {'username': None, 'password': None}},
    "search_movie": {'list': REQUEST_QUERIES, 'params': {'key': None, 'value': None}},
    "search_user": {'list': REQUEST_QUERIES, 'params': {'username': None}},
    "special_movie": {'list': REQUEST_QUERIES, 'params': {'movie_id': 0}},
    "special_user": {'list': REQUEST_QUERIES, 'params': {'username': None}},
    "user_login": {'list': REQUEST_QUERIES, 'params': {'username': None, 'password': None}},
    "user_point": {'list': REQUEST_QUERIES, 'params': {'username': None}},
    "user_wallet": {'list': REQUEST_QUERIES, 'params': {'username': None}},
    "user_watch_special": {'list': REQUEST_QUERIES, 'params': {'pro_id': None}},
    "user_watch": {'list': REQUEST_QUERIES, 'params': {'username': None}}
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
        c.execute(dml_queries[query]['list'][query], inputs)
        connection.commit()
        print("> Commited")
    except Error as e:
        print(e)
        connection.rollback()


def import_temp_data(connection):
    """
    This method imports a template data to our database
    """
    data = load_data()
    for obj in data.values():
        execute_query(connection=connection, query=obj['op'], inputs=list(obj['data'].values()))



if __name__ == '__main__':
    connection = create_connection(DATABASE)
    connection.close()
