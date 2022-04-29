import os

class Board():
    def __init__(self): # Initializing the board
        self.cells = [" "," "," "," "," "," "," "," "," "," "]

    def drawBoard(self):  ## Drawing the board
        print(f'{self.cells[1]} | {self.cells[2]} | {self.cells[3]}')
        print("---------")
        print(f'{self.cells[4]} | {self.cells[5]} | {self.cells[6]}')
        print("---------")
        print(f'{self.cells[7]} | {self.cells[8]} | {self.cells[9]}')
    
    def play(self):
        owrong = True  # This variable to make sure the O player doesn't put a square that's already taken
        self.drawBoard()
        x = int(input('X) Please choose a square from 1-9 >'))
        if self.cells[x] == " ":  ## If the square is empty.
            self.cells[x] = "X"
        else:
            print("Square already taken")
            return
        self.drawBoard()
        if self.isWin("X") == True:
            return
        if self.isTie():
            return
        o = int(input('O) Please choose a square from 1-9 >'))
        while owrong:                   ## Do - while loop to execute at least once. If the squuare is empty break out of the loop.
            if self.cells[o] == " ":
                self.cells[o] = "O"
                owrong=False
            else:
                print("Square already taken")
                o = int(input('O) Please choose a square from 1-9 >'))
    
    def isWin(self,player):  ## This function is to know if a player wins
        if self.cells[1] == player and self.cells[2] == player and self.cells[3] == player:
            return True
        if self.cells[4] == player and self.cells[5] == player and self.cells[6] == player:
            return True
        if self.cells[7] == player and self.cells[8] == player and self.cells[9] == player:
            return True
        if self.cells[1] == player and self.cells[4] == player and self.cells[7] == player:
            return True
        if self.cells[2] == player and self.cells[5] == player and self.cells[8] == player:
            return True
        if self.cells[3] == player and self.cells[6] == player and self.cells[9] == player:
            return True
        if self.cells[1] == player and self.cells[5] == player and self.cells[9] == player:
            return True
        if self.cells[3] == player and self.cells[5] == player and self.cells[7] == player:
            return True
    
    def resetBoard(self): ## This function resets the board in case the players wants to play again.
        self.cells = [" "," "," "," "," "," "," "," "," "," "]
    
    def isTie(self):   ## This function checks if all the cells are filled but no players have won.
        used=0
        for cell in self.cells:
            if cell != " ":
                used+=1
        if used == 9:
            return True
        else:
            return False




if __name__ == "__main__": 
    board = Board()
    while True:
        print("Welcome to Tic Tac Toe")
        board.play()
        if board.isWin("X"):
            print("X wins the game!")
            choice = input("Would you like to play again? (Y/N) > ").upper()
            if choice =="Y":
                board.resetBoard()
            else:
                print("Thanks for playing!")
                break
        if board.isTie():
            print("This round is a tie")
            choice = input("Would you like to play again? (Y/N) > ").upper()
            if choice =="Y":
                board.resetBoard()
            else:
                print("Thanks for playing!")
                break
        if board.isWin("O"):
            print("O Wins the game!")
            choice = input("Would you like to play again? (Y/N) > ").upper()
            if choice =="Y":
                board.resetBoard()
            else:
                print("Thanks for playing!")
                break

    