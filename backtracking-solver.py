#Solver taking the backtracking approach


board = [
            [4,0,0,0,3,0,0,6,0],
            [2,0,0,1,0,0,4,0,0],
            [7,5,0,9,0,4,1,0,0],
            [0,9,0,6,2,8,5,0,4],
            [0,0,2,0,0,0,3,0,0],
            [5,0,4,7,1,3,0,8,0],
            [0,0,8,5,0,1,0,4,7],
            [0,0,7,0,0,6,0,0,1],
            [0,4,0,0,8,0,0,0,9]
        ]
#Walks through each row to print the board. Can be improved to look more user friendly later but not necessary.
def printBoard(board):
    for row in board:
        for column in row:
            print(column, end=" ")
        print()

#This finds an "empty" box on the board, which is shown by an integer 0.
def findEmpty(board):
    for row in range(len(board)):
        for column in range(len(board[0])):
            if board[row][column] == 0:
                return (row, column)

