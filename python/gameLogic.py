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
            "game": {"startScoreP1": 0, "startScoreP2": 0, "maxLongWin": 10},
        }

def fillTable(namep1, namep2, p1score, p2score):
    conn = sqlite3.connect('viebBalldb.sqlite')
    cur = conn.cursor()
    cur.execute('INSERT INTO scores (player1, player2, scorep1, scorep2) values (?, ?, ?, ?)', (namep1, namep2, p1score, p2score))
    conn.commit()
    conn.close()


player1 = "Dan"
player2 = "Lan"

def gameLogic(scoreP1, scoreP2, maxLongWin, maxQuickWin):
    while scoreP1 < maxLongWin and scoreP2 < maxLongWin:
        userInput = input("Who scored? 1 or 2? ")
        if userInput == "1":
            scoreP1 += 1
            print("The current score of player one is " + str(scoreP1))
        else:
            scoreP2 += 1
            print("The current score of player two is " + str(scoreP2))
        if (scoreP1 >= maxQuickWin and scoreP2 == 0) or (scoreP2 >= maxQuickWin and scoreP1 == 0):
            print("Quick Win")
            break
    return scoreP1, scoreP2


def main():
    config = load_config()

    scoreP1 = config["game"]["startScoreP1"]
    scoreP2 = config["game"]["startScoreP2"]
    maxLongWin = config["game"]["maxLongWin"]

    quickWinEnabled = config["rules"].get("quickWin", True)
    maxQuickWin = config["rules"].get("maxQuickWin", 7)

    if quickWinEnabled:
        scoreP1, scoreP2 = gameLogic(scoreP1, scoreP2, maxLongWin, maxQuickWin)
    else:
        scoreP1, scoreP2 = gameLogic(scoreP1, scoreP2, maxLongWin, maxLongWin)

    fillTable(player1, player2, scoreP1, scoreP2)

if __name__ == "__main__":
    main()