import sqlite3
from datetime import datetime

def connectTest(conn):
    """
    Records the time it takes to connect to a sqlite3 database.
    """
    start = datetime.now()
    conn = sqlite3.connect('db.sqlite3')
    end = datetime.now()
    return end - start


def createTable30(conn):
    """
    Returns the time it takes to create a table in a database 30 columns wide.
    """
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
    return end - start


def writeSingle(conn, wordMatrix):
    """
    Returns the time required to commit the first entry in s 2D array to the database.
    wordmatrix is a 30 x N list of strings.
    """
    start = datetime.now()
    conn = sqlite3.connect('db.sqlite3')
    insertCommand = """INSERT INTO randomData VALUES 
        (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);"""
    conn.execute(insertCommand, wordMatrix[0])
    conn.commit()
    conn.close()
    end = datetime.now()
    return end - start


def writeAllWords(conn, wordMatrix):
    """
    Returns the time required to write a 30 x N 2D list of strings to the database.
    """
    start = datetime.now()
    conn = sqlite3.connect('db.sqlite3')
    insertCommand = """INSERT INTO randomData VALUES 
        (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);"""
    for line in wordMatrix:
        conn.execute(insertCommand, line)
        conn.commit()
    conn.close()
    end = datetime.now()
    return end - start


def selectAll(conn):
    """
    Returns the time required to select all columns from the database.
    """
    start = datetime.now()
    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.execute("SELECT * from randomData")
    #for row in cursor:
    #    for entry in row:
    #        print(entry)
    conn.close()
    end = datetime.now()
    return end - start


def selectAs(conn):
    """
    Returns the time required to select all columns from the database.
    """
    start = datetime.now()
    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.execute("SELECT * from randomData where col0 like 'a%'")
    #for row in cursor:
    #    for entry in row:
    #        print(entry)
    conn.close()
    end = datetime.now()
    return end - start


def textTest(wordMatrix):
    conn = sqlite3.connect('db.sqlite3')
    print('Timing initial db connection...')
    conTime = connectTest(conn)
    print(f'done {conTime}')
    print('Timing creation of table 30 wide...')
    createTime = createTable30(conn)
    print(f'done {createTime}')
    print('Timing single line entry...')
    writeSinTime = writeSingle(conn, wordMatrix)
    print(f'done {writeSinTime}')
    print(f'Timing entry of {len(wordMatrix)} lines...')
    writeAllTime = writeAllWords(conn, wordMatrix)   
    print(f'done {writeAllTime}')
    print('Timing "select *"')
    selAllTime = selectAll(conn)
    print(f'done {selAllTime}')
    print('Timing "select * where col0 like \'a%\'"')
    selAs = selectAll(conn)
    print(f'done {selAllTime}')

    total = conTime + createTime + writeSinTime + writeAllTime + selAllTime + selAs
    print(f'Total time: {total}')
    print(f'Total sans writeAll: {total - writeAllTime}')


