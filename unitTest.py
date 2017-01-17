# -*- coding: utf-8 -*-
"""
@author: grinch
"""

'''
Unit tests for connect4.py
'''
import unittest
from connect4 import Game
import test_boardStates as testBoards

class StartGameTest(unittest.TestCase):
    """Tests for all possible functions and winner/add piece/invalid moves"""

    def setUp(self):
        self.game = Game()
        
    ############CHECK PLAYER'S COLOR PICK############    
    def test_playerPicksColor(self):
        """Test if a player's choice of white is set."""
        print "test_playerPicksColor"
        self.game.startGame("white")
        self.assertEqual("white", self.game.answer)

    def test_playerPickNoColor(self):
        """Test if a player's non-selection of choice sets black."""
        print "test_playerPickNoColor"
        self.game.startGame()
        self.assertEqual("black", self.game.answer)
        
    ############CHECK NEW BOARD CREATION############
    def test_createBoard(self):
        """Test to check a new board initialization is right."""
        print "test_createBoard"
        self.assertEqual = (testBoards.New_board, self.game.board)
        
    ############CHECK FOR MOVE VALIDITY############    
    def test_validMove(self):
        """Test adding a piece to the board."""
        print "test_validMove"
        self.game.board = testBoards.Full_column
        self.game.makeMove(1, 1)
        self.assertEqual(testBoards.After_add, self.game.board)

    def test_invalidCol_message(self):
        """Returns 'invalid' if trying to add a piece to the board outside of it's range."""
        print "test_invalidCol_message"
        result = self.game.humanMoves(0)
        self.assertEqual("Invalid", result)

    def test_invalidCol_board(self):
        """Board does not update/add piece if column number is out of range."""
        print "test_invalidCol_board"
        self.game.humanMoves(0)
        self.assertEqual(testBoards.New_board, self.game.board)
    
    def test_fullCol_false(self):
        """Returns false if unable to add a piece to a full column."""
        print "test_fullCol_false"
        self.game.board = testBoards.Full_column
        result = self.game.makeMove(0, 1)
        self.assertFalse(False, result)
        
    def test_fullCol_board(self):
        """Board does not update/add piece if column is full."""
        print "test_fullCol_board"
        self.game.board = testBoards.Full_column
        self.game.makeMove(0, 1)
        self.assertEqual(testBoards.Full_column, self.game.board)
        
    ############CHECK FOR WINS############    
    def test_humanVerticalWin(self):
        """Test for human's vertical win."""
        print "test_humanVerticalWin"
        self.game.board = testBoards.Human_win_vertical
        result = self.game.gameStatus()
        self.assertEqual(2, result)

    def test_aiVerticalWin(self):
        """Test for AI's vertical win."""
        print "test_aiVerticalWin"
        self.game.board = testBoards.AI_win_vertical
        result = self.game.gameStatus()
        self.assertEqual(1, result)

    def test_humanHorizontalWin(self):
        """Test for human's horizontal win."""
        print "test_humanHorizontalWin"
        self.game.board = testBoards.Human_win_horizontal
        result = self.game.gameStatus()
        self.assertEqual(2, result)

    def test_aiHorizontalWin(self):
        """Test for AI's horizontal win."""
        print "test_aiHorizontalWin"
        self.game.board = testBoards.AI_win_horizontal
        result = self.game.gameStatus()
        self.assertEqual(1, result)

    ############CHECK FOR TIE############
    def test_noWinner(self):
        """Test if a tie/draw is detected and returned correctly."""
        print "test_noWinner"
        self.game.board = testBoards.Tied_game_board
        result = self.game.gameStatus()
        self.assertEqual(0, result)
        
if __name__ == '__main__':
    unittest.main()