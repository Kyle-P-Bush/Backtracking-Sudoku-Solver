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
def solve(board):
    find = findEmpty(board)
    if not find:
        return True
    else:
        row, column = find
    for i in range(1,10):
        if isValid(board, i, (row, column)):
            board[row][column] = i

            if solve(board):
                return True
            board[row][column] = 0
    return False

#Check for a valid number based on the constrictions.
#Takes in the board, a number to try, and the position within the board.
#   Note: position is represented as positon[row, column]
def isValid(board, number, position):

    #Check if the number is in the row

    for i in range(len(board[0])):
        #Checks each column within a row (pos will be a tuple (row, column)) and sees if it is equal to
        #the number that was just added. However, the position[1] != i makes sure that we skip the position
        #we just added the number to since theres no need to check that.
        if board[position[0]][i] == number and position[1] != i:
            return False
    

    #Check if the number is in the column
    
    for i in range(len(board)):
        if board[i][position[1]] == number and position[0] != i:
            return False

    #Check if the number is in the 3x3 Block
    box_x = position[1] // 3
    box_y = position[0] // 3
    #TODO: Add description of logic
    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x*3, box_x*3 +3):
            if board[i][j] == number and (i,j) != position:
                return False
    
    return True

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
    return None

printBoard(board)
solve(board)
print("---------")
printBoard(board) 
