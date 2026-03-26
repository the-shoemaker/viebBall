import tomllib
from pathlib import Path
import sqlite3

def load_config():
    config_path = Path(__file__).with_name("config.toml")
    try:
        with config_path.open("rb") as f:
            return tomllib.load(f)
    except FileNotFoundError:
        return {
            "rules": {"quickWin": True, "maxQuickWin": 7},
            "game": {"maxLongWin": 10}
        }


def fillTable(namep1, namep2, p1score, p2score):
    conn = sqlite3.connect('viebBalldb.sqlite')
    cur = conn.cursor()
    cur.execute('INSERT INTO scores (player1, player2, scorep1, scorep2) values (?, ?, ?, ?)', (namep1, namep2, p1score, p2score))
    conn.commit()
    conn.close()


def gameLogic(p1, scoreP1, scoreP2, maxLongWin, maxQuickWin):
    gameOver = False
    if p1 == 1:
        scoreP1 += 1
        print("The current score of player one is " + str(scoreP1))
    else:
        scoreP2 += 1
        print("The current score of player two is " + str(scoreP2))

    if (scoreP1 >= maxQuickWin and scoreP2 == 0) or (scoreP2 >= maxQuickWin and scoreP1 == 0):
        gameOver = True
        print("Quick Win")
    elif scoreP1 >= maxLongWin or scoreP2 >= maxLongWin:
        gameOver = True
        print("Long Win")

    return scoreP1, scoreP2, gameOver

