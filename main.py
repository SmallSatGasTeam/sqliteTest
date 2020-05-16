import sqlite3
from datetime import datetime

from helpers import twoDize, printArray

def getWords():
    words = []
    with open('/usr/share/dict/words') as f:
        for line in f:
            words.append(f.readline().strip())
    return words

def textTest(wordMatrix):
    #####################
    # Connect to Database
    #####################
    print('connecting to database')
    start = datetime.now()

    conn = sqlite3.connect('db.sqlite3')
    c = conn.cursor()

    end = datetime.now()
    print(f'done {end - start}\n')

    ##############
    # Create Table
    ##############
    print('creating 30 column database table')
    start = datetime.now()

    c.execute('''CREATE TABLE IF NOT EXISTS randomData
            (
            col0 text,
            col1 text,
            col2 text,
            col3 text,
            col4 text,
            col5 text,
            col6 text,
            col7 text,
            col8 text,
            col9 text,
            col10 text,
            col11 text,
            col12 text,
            col13 text,
            col14 text,
            col15 text,
            col16 text,
            col17 text,
            col18 text,
            col19 text,
            col20 text,
            col21 text,
            col22 text,
            col23 text,
            col24 text,
            col25 text,
            col26 text,
            col27 text,
            col28 text,
            col29 text
            )''')
    conn.close()

    end = datetime.now()
    print(f'done {end - start}\n')

    #############
    # Write words 
    #############
    print('writing words to database')
    start = datetime.now()

    conn = sqlite3.connect('db.sqlite3')
    c = conn.cursor()

    for line in wordMatrix:

        c.execute(f"INSERT INTO randomData VALUES ('{line[0]}','{line[1]}','{line[2]}','{line[3]}','{line[4]}','{line[5]}','{line[6]}','{line[7]}','{line[8]}','{line[9]}','{line[10]}','{line[11]}','{line[12]}','{line[13]}','{line[14]}','{line[15]}','{line[16]}','{line[17]}','{line[18]}','{line[19]}','{line[20]}','{line[21]}','{line[22]}','{line[23]}','{line[24]}','{line[25]}','{line[26]}','{line[27]}','{line[28]}','{line[29]}')")
    
    con.close()

    end = datetime.now()
    print(f'done {end - start}\n')
    
    #######################
    # Select all from table
    #######################
    print('selecting * from table')
    start = datetime.now()

    conn = sqlite3.connect('db.sqlite3')
    c = conn.cursor()

    con.close()

    end = datetime.now()
    print(f'done {end - start}\n')


if __name__ == '__main__':
    tableWidth = 30
    words = getWords()
    print('Performing sqlite test for text datatype')
    print(f'{len(words)} words read from system dictionary')
    wordMatrix = twoDize(words, tableWidth)
    print(f'Dictionary reshaped to a width of {tableWidth}\n')
    textTest(wordMatrix)    

