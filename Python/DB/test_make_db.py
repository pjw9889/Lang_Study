import sqlite3

def create_table():

    connect = sqlite3.connect('test.db')

    cur = connect.cursor()

    cur.execute(''' CREATE TABLE test (
                        title text,
                        published_date text,
                        publisher text,
                        pages integer,
                        recommendation integer
                    )'''
               )
    connect.commit()

    connect.close()

if __name__ == "__main__":

    create_table()
