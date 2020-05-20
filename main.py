import sqlite3
from datetime import datetime

from src.textTest import textTest
from src.helpers import twoDize, printArray, getWords

if __name__ == '__main__':
    tableWidth = 30
    words = getWords()
    print('Performing sqlite test for text datatype')
    print(f'{len(words)} words read from system dictionary')
    wordMatrix = twoDize(words, tableWidth)
    print(f'Dictionary reshaped to a width of {tableWidth}\n')
    textTest(wordMatrix)    

