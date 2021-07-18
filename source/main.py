import sqlite3 
from sqlite3 import Error
from sys import exec_prefix
from createDB import create_connection, create_database
import os



DEF_DIR = './database/'
DATABASE = DEF_DIR + 'stream.db'

INIT_DIR = './sql/table/'
INIT_PART = ['entity/', 'relation/']

def get_initilize_queries():
    init_queries = []
    for part in INIT_PART:
        address = INIT_DIR + part
        onlyfiles = [f for f in os.listdir(address)]
        for file in onlyfiles:
            with open(address + file, 'r') as myFile:
                query = myFile.read()
                init_queries.append(query)
    return init_queries


def initialize_tables(connection, queries):
    c = connection.cursor()
    count = 0
    for query in queries:
        try:
            c.execute(query)
        except Error as e:
            count += 1
            print(e)
    print("Error: " + str(count))



if __name__ == '__main__':
    create_database(DATABASE)
    connection = create_connection(DATABASE)
    init = get_initilize_queries()
    initialize_tables(connection, init)
    connection.close()