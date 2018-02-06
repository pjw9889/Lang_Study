import sqlite3

def insert_text():
    conn = sqlite3.connect('test.db')
    cur = conn.cursor()

    insert_sql = 'INSERT INTO test VALUES (?,?,?,?,?)'

    cur.execute(insert_sql, ('Developer', '2015.03.02', 'A', 200, 0))

    books = {
        ('big data', '2013.03.02', 'B', 296, 1),
        ('Google', '2011.01.11', 'C', 555, 3),
        ('Lector', '2017.03.22', 'D', 777, 4)
    }

    cur.executemany(insert_sql, books)

    conn.commit()
    conn.close()

if __name__ =="__main__":

    insert_text()
