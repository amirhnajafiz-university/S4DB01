"""
This file is the setup of our project,
where we create the database of SQLite3 and we
create our tables.

"""
import sqlite3 
from sqlite3 import Error
import os


MAIN_DIR = './sql/'
INIT_DIR = MAIN_DIR + 'table/'
INIT_PART = ['entity/', 'relation/']


def create_database(db_file):
    """ Create a database file based on SQLite """
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


def get_initialize_queries():
    """ This function gets the Queries that we need to build the database tables """
    init_queries = []
    for part in INIT_PART:
        address = INIT_DIR + part
        onlyfiles = [f for f in os.listdir(address)]
        for file in onlyfiles:
            with open(address + file, 'r') as myFile:
                query = myFile.read()
                init_queries.append(query)
    return init_queries


def initialize_tables(connection):
    """ This function builds the database tables from the initialize queries """
    c = connection.cursor()
    queries = get_initialize_queries()
    count = 0
    for query in queries:
        try:
            c.execute(query)
        except Error as e:
            count += 1
            print(e)
    print("Error: " + str(count))
