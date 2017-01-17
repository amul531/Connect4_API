# -*- coding: utf-8 -*-
"""
@author: grinch
"""

'''
This is not a unit test. 
Testing the game to check if the winner(not a tie) part of the code works.
There is no error handling here since it's now a part of the API. Instead on invalid moves, your turn just gets skipped
'''
from connect4 import Game as g

def testGame():
	game = g()

	print game.printBoard()

	for i in range(0, 10): 
         print "\n"
         col = int(input("Human, your turn to make a move(1-7): ")) 
         game.humanMoves(col)
         
         # Check for a consecutive 4 (connect 4)
         print game.printBoard()
         
         result = game.gameStatus()
         if result==2:
             print "You won!"
             break
         
         print "\n"
         print "Now the AI makes it's move: "
         
         # Find the best move for the AI
         aiMove = game.compMoves()
         game.makeMove(aiMove, 1)
         result = game.gameStatus()
         
         #Check for a consecutive 4 (connect 4)
         print game.printBoard()
         if result==1:
             print "AI won!\n"
             break

                		
testGame()

while raw_input("Play again? (y/n) ") == "y": 
	print "Let's do this!"
	testGame()

