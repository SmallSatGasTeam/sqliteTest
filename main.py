import sqlite3

words = []

with open('/usr/share/dict/words') as f:
    words.append(f.read())

#TODO: put words in an nx30 array and commmit each line to the database and time it.  
conn = sqlite3.connect('db.sqlite3')
c = conn.cursor()

# Create Table
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


conn = sqlite3.connect('db.sqlite3')
c = conn.cursor()

#TODO: select various sets from database and time it.  
