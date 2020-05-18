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

    end = datetime.now()
    print(f'done {end - start}\n')

    ##############
    # Create Table
    ##############
    print('creating 30 column database table')
    start = datetime.now()

    conn.execute('''CREATE TABLE IF NOT EXISTS randomData
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

    ##################
    # Write single row 
    ##################
    print('writing single row to database')
    start = datetime.now()

    conn = sqlite3.connect('db.sqlite3')

    insertCommand = """INSERT INTO randomData VALUES 
        (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);"""
    
    conn.execute(insertCommand, wordMatrix[0])
    conn.commit()
    
    conn.close()

    end = datetime.now()
    print(f'done {end - start}\n')
 
    #############
    # Write words 
    #############
    print('writing words to database')
    start = datetime.now()

    conn = sqlite3.connect('db.sqlite3')

    insertCommand = """INSERT INTO randomData VALUES 
        (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);"""
    
    for line in wordMatrix:
        conn.execute(insertCommand, line)
        conn.commit()
    
    conn.close()

    end = datetime.now()
    print(f'done {end - start}\n')
    
    #######################
    # Select all from table
    #######################
    print('selecting * from table')
    start = datetime.now()

    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.execute("SELECT * from randomData where col0 like 'a%'")
    #cursor = conn.execute("SELECT * from randomData")
    
    #for row in cursor:
    #    for entry in row:
    #        print(entry)

    conn.close()

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

