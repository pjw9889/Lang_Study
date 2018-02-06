#some select
import sqlite3
import sys

def select_some(number):

    conn = sqlite3.connect('test.db')
    cur = conn.cursor()

    cur.execute('SELECT * FROM test')
    # if you want to more detail condition -> use detail SQL
    print('[2] some data print')
    books = cur.fetchmany(int(number))
    # if you want to only one -> use "fetchone"

    for book in books:
        print(book)

    conn.close()

if __name__ == "__main__":

    select_some(sys.argv[1])
