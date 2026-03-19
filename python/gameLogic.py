def gameLogic(scorePlayerOne, scorePlayerTwo):
    while scorePlayerOne < 10 and scorePlayerTwo < 10:
        userInput = input("Who scored? 1 or 2? ")
        if userInput == "1":
            scorePlayerOne += 1
            print("The current score of player one is " + str(scorePlayerOne))
        else:
            scorePlayerTwo += 1
            print("The current score of player two is " + str(scorePlayerTwo))

scorePlayerOne = 0
scorePlayerTwo = 0

gameLogic(scorePlayerOne, scorePlayerTwo)