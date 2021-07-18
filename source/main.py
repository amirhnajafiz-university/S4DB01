import sqlite3 
from sqlite3 import Error
from sys import exec_prefix
from createDB import create_connection, create_database, initialize_tables
from queries import INSERT_QUERIES, DELETE_QUERIES, UPDATE_QUERIES



DEF_DIR = './database/'
DATABASE = DEF_DIR + 'stream.db'


if __name__ == '__main__':
    #create_database(DATABASE)
    #connection = create_connection(DATABASE)
    #initialize_tables(connection)
    #connection.close()
    pass