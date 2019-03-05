from GameEntry import GameEntry
from Scoreboard import Scoreboard


if __name__ == '__main__':
    scoreBoard = Scoreboard()
    don = GameEntry("don", 200)
    #print(don)
    jane = GameEntry("jane", 100)
    #print(jane)
    james = GameEntry("james", 50) 
    scoreBoard.add(don)
    scoreBoard.add(jane)
    scoreBoard.add(james)
    print(scoreBoard)