"""
This package opens the sql files and generates our
queries from the files content, into seperate dictionaries,
where we can use them later.

"""
import os 
from createDB import MAIN_DIR



DELETE_DIR = MAIN_DIR + '/delete/'
INSERT_DIR = MAIN_DIR + '/insert/'
UPDATE_DIR = MAIN_DIR + '/update/'

DELETE_QUERIES = {}
INSERT_QUERIES = {}
UPDATE_QUERIES = {}


def init(address, dic):
    onlyfiles = [f for f in os.listdir(address)]
    for file in onlyfiles:
        with open(address + file, 'r') as myFile:
            dic[file[:-4]] = myFile.read()


init(DELETE_DIR, DELETE_QUERIES)
init(INSERT_DIR, INSERT_QUERIES)
init(UPDATE_DIR, UPDATE_QUERIES)
