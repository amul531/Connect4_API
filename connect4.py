# -*- coding: utf-8 -*-
"""
@author: grinch
"""
import sys
import random

class Game:
    def __init__(self):
        """
        Create a new board for the game.
        Generate a unique/random gameID to keep track of a game.
        """
        self.board = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0]
        ]        
        self.gameId = int(random.random()*1000);

    def calculateScore(self, aiScore, moreMoves): 
        """
        Calculates the score to help decide the AI's next move
        :param aiScore: the # of consecutive AI pieces so far
        :param moreMoves: the # of moves left to get 4 consecutive pieces
        :return: an int value
        """
        moveScore = 4 - moreMoves;
        if aiScore==0:
            return 0
        elif aiScore==1:
            return 1*moveScore
        elif aiScore==2:
            return 10*moveScore
        elif aiScore==3:
            return 100*moveScore
        else:
            return 1000

    def evalBoard(self):  
        """
        Evaluate the board for AI
        :return: an int value
        """
        aiScore=1
        score=0
        blanks = 0
        k=0
        moreMoves=0
        for i in range(5, -1, -1):  
            for j in range(0, 7):  
                if self.board[i][j] != 1:
                    continue
                #Value moving right from each spot
                if j<=3:
                    for k in range(1, 4):  
                        if self.board[i][j+k]==1:
                            aiScore+=1
                        elif self.board[i][j+k]==2:
                            aiScore=0
                            blanks = 0
                            break
                        else:
                            blanks+=1
                    moreMoves = 0
                    if blanks>0:
                        for c in range(1, 4):  
                            column = j+c
                            for m in range(i, 6):  
                                if self.board[m][column]==0:
                                    moreMoves+=1
                                else:
                                    break
                    if moreMoves!=0:
                        score += self.calculateScore(aiScore, moreMoves)
                    aiScore=1
                    blanks = 0
                    
                #Value moving right from each spot
                if j>=3:
                    for k in range(1, 4):  
                        if self.board[i][j-k]==1:
                            aiScore+=1
                        elif self.board[i][j-k]==2:
                            aiScore=0
                            blanks=0
                            break
                        else:
                            blanks+=1
                    moreMoves=0
                    if blanks>0:
                        for c in range(1, 4):  
                            column = j- c
                            for m in range(i, 6):  
                                if self.board[m][column]==0:
                                    moreMoves+=1
                                else:
                                    break
                    if moreMoves!=0:
                        score += self.calculateScore(aiScore, moreMoves)
                    aiScore=1
                    blanks = 0
                    
                #Value moving down from each spot
                if i>=3:
                    for k in range(1, 4):  
                        if self.board[i-k][j]==1:
                            aiScore+=1
                        elif self.board[i-k][j]==2:
                            aiScore=0
                            break
                    moreMoves = 0
                    if aiScore>0:
                        column = j
                        for m in range(i-k+1, i):  
                            if self.board[m][column]==0:
                                moreMoves+=1
                            else:
                                break
                    if moreMoves!=0:
                        score += self.calculateScore(aiScore, moreMoves)
                    aiScore=1
                    blanks = 0
                    
                #Value heading diagonal (lower-left:'/') from each spot
                if i>=3 and j<=3:
                    for k in range(1, 4):  
                        if self.board[i-k][j+k]==1:
                            aiScore+=1
                        elif self.board[i-k][j+k]==2:
                            aiScore=0
                            blanks=0
                            break
                        else:
                            blanks+=1
                    moreMoves=0
                    if blanks>0:
                        for c in range(1, 4):  
                            column = j+c
                            row = i-c
                            for m in range(row, 6): 
                                if self.board[m][column]==0:
                                    moreMoves+=1
                                elif self.board[m][column]==1:
                                    continue
                                else:
                                    break
                        if moreMoves != 0:
                            score += self.calculateScore(aiScore, moreMoves)
                        aiScore=1
                        blanks =0
                        
                #Value heading diagonal (lower-right:'\') from each spot:
                if i>=3 and j>=3:
                    for k in range(1, 4):  
                        if self.board[i-k][j-k]==1:
                            aiScore+=1
                        elif self.board[i-k][j-k]==2:
                            aiScore=0
                            blanks=0
                            break
                        else:
                            blanks+=1
                    moreMoves=0
                    if blanks>0:
                        for c in range(1, 4):  
                            column = j-c
                            row = i-c
                            for m in range(row, 6):  
                                if self.board[m][column]==0:
                                    moreMoves+=1
                                elif self.board[m][column]==1:
                                    continue
                                else:
                                    break
                        if moreMoves!=0:
                            score += self.calculateScore(aiScore, moreMoves)
                        aiScore=1
                        blanks = 0
        return score

    def undoMove(self, col):
        """
        Undoes the move simulated by the AI
        :param col: column to remove piece from
        """
        for i in range(0, 6):  
            if self.board[i][col] != 0:
                self.board[i][col] = 0
                break 

    def minimax(self, depth, turn):  
        """
        Minimax algorith implementation for the AI
        :param depth:
        :param turn:
        :return: maxScore if it's AI's turn else minScore
        """
        maxDepth = 5
        gameResult = self.gameStatus()
        if gameResult==1:
            return sys.maxint
        elif gameResult==2:
            return -sys.maxint
        elif gameResult==0:
            return 0
        if depth==maxDepth:
            return self.evalBoard()
        maxScore= -sys.maxint
        minScore = sys.maxint
        for j in range(0, 7):  
            if self.board[0][j] !=0:
                continue  #if the move is illegal, continue
            if turn==1:  #comp looks to maximize it's score during it's turn
                self.makeMove(j, 1)
                currentScore = self.minimax(depth+1, 2)
                maxScore = max(currentScore, maxScore)
                if depth==0:
                    if maxScore==currentScore:
                        self.compLoc = j
                    if maxScore==sys.maxint:  #If Ai is going to win, play here, no need of further evaluation
                        self.undoMove(j)
                        break
            elif turn==2: #comp looks to minimize human's score during it's turn
                self.makeMove(j, 2)
                currentScore = self.minimax(depth+1, 1)
                minScore = min(currentScore, minScore)
            self.undoMove(j)
        return maxScore if turn==1 else minScore

    def compMoves(self):
        """
        AI picks a move
        :return: the column where the move is to be made
        """
        self.compLoc = -1
        self. minimax(0, 1) #sets the comp's location to max if comp's turn else min
        return self.compLoc

    def isBoardFull(self):
        """
        Checks if the board is filled
        :return -1: if it's not
        """
        for j in range(0, 7):  
            if self.board[0][j]==0:
                return -1

    def gameStatus(self): 
        """
        Checks the game(board) status : if win/draw/not over
        :return 0: if it's a draw
        :return 1: if AI wins
        :return 2: if human wins
        :return -1: if neither
        """
        compScore = 0
        humanScore = 0
        full = 3
        #Check for a winner
        for i in range(5, -1, -1):  
            for j in range(0, 7):  
                '''
                if self.board[i][j]==0:
                    continue
                '''
                #Check for a horizontal win
                if j<=3:
                    for k in range(0,4): 
                        if self.board[i][j+k]==1:
                            compScore+=1
                        elif self.board[i][j+k]==2:
                            humanScore+=1
                        else:
                            break
                    if compScore==4:
                        return 1
                    elif humanScore==4:
                        return 2
                    compScore = 0
                    humanScore = 0

                #Check for a vertical win
                if i>=3:
                    for k in range(0,4):
                        if self.board[i-k][j]==1:
                            compScore+=1
                        elif self.board[i-k][j]==2:
                            humanScore+=1
                        else:
                            break
                    if compScore==4:
                        return 1
                    elif humanScore==4:
                        return 2
                    compScore = 0
                    humanScore = 0

                #Check for a diagonal(/) win
                if j<=3 and i>= 3:
                    for k in range(0,4): 
                        if self.board[i-k][j+k]==1:
                            compScore+=1
                        elif self.board[i-k][j+k]==2:
                            humanScore+=1
                        else:
                            break
                    if compScore==4:
                        return 1
                    elif humanScore==4:
                        return 2
                    compScore = 0
                    humanScore = 0

                #Check for a diagonal(\) win
                if j>=3 and i>=3:
                    for k in range(0,4): 
                        if self.board[i-k][j-k]==1:
                            compScore+=1
                        elif self.board[i-k][j-k]==2:
                            humanScore+=1
                        else:
                            break
                    if compScore==4:
                        return 1
                    elif humanScore==4:
                        return 2
                    compScore = 0
                    humanScore = 0
        #check for winner is over

        #Check if board is full: return -1 if it's not
        full = self.isBoardFull()
        if full == -1:
            return full
        
        #If board is filled and no winner: return 0 to indicate a draw
        return 0
           
    def printBoard(self):
        # Flip the board upside down, so 0,0 is bottom left instead of top left, then print each row
        for line in self.board:
            print "|",
            for cell in line:
                print "H" if cell == 2 else "C" if cell else ".",
            print "|"

    def makeMove(self, col, player):
        """
        Places the piece in a particular column (if possible)
        :param col: column to add piece to
        :param player: player piece to add to board
        :return: (boolean) if piece was successfully added
        """
        for i in range(5, -1, -1):  
            if self.board[i][col] == 0:
                self.board[i][col] = player 
                return True
        return False
           
    #Human make a move
    def humanMoves(self, col):
        if col<1  or col>7 or self.board[0][col-1] != 0 :  #Move is illegal
            return "Invalid"
        self.makeMove(col-1, 2) 

    #Start a new game : set the board and generate an id   
    def startGame(self, color="black"):
        self.answer = color
        #If white is picked, let human make first move; else computer makes a move
        if self.answer=="white":
            return self.gameId, self.board
        print "Computer's move: ",4
        self.makeMove(4-1, 1)
        return self.gameId, self.board
            
    #The game in progress
    def playGame(self, playerMove):
       if self.humanMoves(playerMove) != "Invalid":
           result = self.gameStatus()
           if result==2:
               return result, self.board
           elif result==0:
               return result, self.board
           #Computer makes a move
           aiMove = self.compMoves()
           self.makeMove(aiMove, 1)
           result = self.gameStatus()
           if result==1:
               return result, self.board, aiMove+1
           elif result==0:
               return result, self.board, aiMove+1
           return result, self.board, aiMove+1
       else:
           return "Invalid"
           

