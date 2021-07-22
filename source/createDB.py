"""
This file is the setup of our project,
where we create the database of SQLite3 and we
create our tables.

"""
import sqlite3 
from sqlite3 import Error
import os
from sqlite3.dbapi2 import Connection, connect
from main import DATABASE


MAIN_DIR = './sql/'
INIT_DIR = MAIN_DIR + 'table/'
INIT_PART = ['entity/', 'relation/']

TRIGGER_DIR = MAIN_DIR + 'trigger/'


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

    initialize_triggers(connection=connection)


def initialize_triggers(connection):
    c = connection.cursor()
    onlyfiles = [f for f in os.listdir(TRIGGER_DIR)]
    for file in onlyfiles:
        with open(TRIGGER_DIR + file, 'r') as myFile:
            query = myFile.read()
            try:
                c.executescript(query)
                print(f"> Trigger {file} added")
            except Error as e:
                print(e)


if __name__ == "__main__":
    create_database(db_file=DATABASE)
    connection = create_connection(db_file=DATABASE)
    initialize_tables(connection=connection)
    initialize_triggers(connection=connection)
    connection.close()