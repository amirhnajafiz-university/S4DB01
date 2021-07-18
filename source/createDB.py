import sqlite3 
from sqlite3 import Error



def create_database(db_file):
    """ Create a database connection to a SQLite database """
    connection = None

    try:
        connection = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if connection:
            connection.close()


def create_connection(db_file):
    """ Create a database connection to a SQLite database """
    connection = None

    try:
        connection = sqlite3.connect(db_file)
        print(f'Connected :: {sqlite3.version}')
        return connection
    except Error as e:
        print(e)
    finally:
        return connection
