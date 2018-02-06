# All Select
import sqlite3
def select_all():
    conn = sqlite3.connect('test.db')
    cur = conn.cursor()

    cur.execute('SELECT * FROM test')

    print('[1] Data all print')

    books = cur.fetchall()

    for book in books:
        print(book)

    conn.close()

if __name__ =="__main__":

    print("==================================")
    select_all()
