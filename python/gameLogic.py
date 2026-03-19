import tomllib
from pathlib import Path

def load_config():
    config_path = Path(__file__).with_name("config.toml")
    try:
        with config_path.open("rb") as f:
            return tomllib.load(f)
    except FileNotFoundError:
        return {
            "rules": {"quickWin": True, "maxQuickWin": 7},
            "game": {"startScoreP1": 0, "startScoreP2": 0},
        }


def gameLogic(scoreP1, scoreP2, maxQuickWin):
    while scoreP1 < 10 and scoreP2 < 10:
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


def main():
    config = load_config()

    scoreP1 = config["game"]["startScoreP1"]
    scoreP2 = config["game"]["startScoreP2"]

    quickWinEnabled = config["rules"].get("quickWin", True)
    maxQuickWin = config["rules"].get("maxQuickWin", 7)

    if quickWinEnabled:
        gameLogic(scoreP1, scoreP2, maxQuickWin)
    else:
        gameLogic(scoreP1, scoreP2, 10)


if __name__ == "__main__":
    main()