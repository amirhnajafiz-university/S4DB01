import sqlite3
from sqlite3 import Error
from createDB import create_connection, create_database, initialize_tables



DEF_DIR = './database/'
DATABASE = DEF_DIR + 'stream.db'

dml_queries = {
    "insert_admin": { 'list': INSERT_QUERIES, 'params': {'username': None, 'password': None} },
    "insert_admin": { 'list': INSERT_QUERIES, 'params': {} },
    "insert_admin": { 'list': INSERT_QUERIES, 'params': {} },
    "insert_admin": { 'list': INSERT_QUERIES, 'params': {} },
    "insert_admin": { 'list': INSERT_QUERIES, 'params': {} },
    "insert_admin": { 'list': INSERT_QUERIES, 'params': {} },
    "insert_admin": { 'list': INSERT_QUERIES, 'params': {} },
    "insert_admin": { 'list': INSERT_QUERIES, 'params': {} },
    "insert_admin": { 'list': INSERT_QUERIES, 'params': {} },
    "insert_admin": { 'list': INSERT_QUERIES, 'params': {} },
    "insert_admin": { 'list': INSERT_QUERIES, 'params': {} },
    "insert_admin": { 'list': INSERT_QUERIES, 'params': {} },
    "insert_admin": { 'list': INSERT_QUERIES, 'params': {} },
    "insert_admin": { 'list': INSERT_QUERIES, 'params': {} },
    "insert_admin": { 'list': INSERT_QUERIES, 'params': {} },
    "insert_admin": { 'list': INSERT_QUERIES, 'params': {} },
    "insert_admin": { 'list': INSERT_QUERIES, 'params': {} },
    "insert_admin": { 'list': INSERT_QUERIES, 'params': {} },
    "insert_admin": { 'list': INSERT_QUERIES, 'params': {} },
    "insert_admin": { 'list': INSERT_QUERIES, 'params': {} },
    "insert_admin": { 'list': INSERT_QUERIES, 'params': {} },
    "insert_admin": { 'list': INSERT_QUERIES, 'params': {} },
    "insert_admin": { 'list': INSERT_QUERIES, 'params': {} },
    "insert_admin": { 'list': INSERT_QUERIES, 'params': {} }
}


def init():
    """
    By running this method, we create our database and tables.

    """
    create_database(db_file=DATABASE)
    connection = create_connection(db_file=DATABASE)
    initialize_tables(connection=connection)
    connection.close()


def deleteAllTables(connection):
    """
    This method uses the delete tables query to clear the whole database.
    """
    try:
        c = connection.cursor()
        c.executescript(DELETE_QUERIES['delete_tables'])
    except Error as e:
        print(e)
        connection.rollback()


def clearAllTables(connection):
    """
    This method uses the clear tables query to clear the tables content.
    """
    try:
        c = connection.cursor()
        c.executescript(DELETE_QUERIES['clear_tables'])
    except Error as e:
        print(e)
        connection.rollback()


def addAdmin(connection, username, password):
    try:
        c = connection.cursor()
        c.execute(INSERT_QUERIES['insert_admin'], [username, password])
        connection.commit()
    except Error as e:
        print(e)
        connection.rollback()


if __name__ == '__main__':
    from queries import INSERT_QUERIES, DELETE_QUERIES, UPDATE_QUERIES
    connection = create_connection(DATABASE)
    connection.close()