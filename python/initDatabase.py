import sqlite3

def createDB():
    conn = sqlite3.connect('viebBalldb.sqlite')
    conn.close()


def createTables():
    conn = sqlite3.connect('viebBalldb.sqlite')
    cur = conn.cursor()
    cur.execute('CREATE TABLE scores (player1 VARCHAR, player2 VARCHAR, scorep1 INT, scorep2 INT)')
    conn.commit()

    conn.close()


def fillTable():
    conn = sqlite3.connect('viebBalldb.sqlite')
    cur = conn.cursor()
    cur.execute('INSERT INTO scores (player1, player2, scorep1, scorep2) values ("Dan", "Lan", 2, 10)')
    conn.commit()

#createDB()
#createTables()
fillTable()