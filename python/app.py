from flask import Flask, render_template, request
from gameLogic import load_config, gameLogic, fillTable

app = Flask(__name__, template_folder='../html/templates', static_folder='../css/static')

currentP1 = 0
currentP2 = 0
@app.route('/', methods=['GET', 'POST'])
def button():
    global currentP1, currentP2

    config = load_config()
    maxLongWin = config["game"]["maxLongWin"]
    player1 = config["game"]["nameP1"]
    player2 = config["game"]["nameP2"]

    quickWinEnabled = config["rules"].get("quickWin", True)
    maxQuickWin = config["rules"].get("maxQuickWin", 7)

    if request.method == "POST":
        clickedPlayer = int(request.form.get("player", 1))

        if quickWinEnabled:
            currentP1, currentP2, gameOver = gameLogic(clickedPlayer, currentP1, currentP2, maxLongWin, maxQuickWin)
        else:
            currentP1, currentP2, gameOver = gameLogic(clickedPlayer, currentP1, currentP2, maxLongWin, maxLongWin)

        if gameOver:
            fillTable(player1, player2, currentP1, currentP2)
            finalP1 = currentP1
            finalP2 = currentP2
            currentP1 = 0
            currentP2 = 0
            return f"<h1>Game Over!</h1><h2>Final Score: {player1} ({finalP1}) - {player2} ({finalP2})</h2><br><a href='/'>Play Again</a>"

    return render_template("index.html", buttonPressedP1=currentP1, buttonPressedP2=currentP2, playerName1=player1, playerName2=player2)


if __name__ == '__main__':
    app.run(debug=False)