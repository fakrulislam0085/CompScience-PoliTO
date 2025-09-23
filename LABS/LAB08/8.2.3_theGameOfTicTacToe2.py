# Solution 2
# Use camelCase 

def displayGameBoard(gameBoard) : 
    for row in gameBoard : 
        # print(f"{' '.join([element for element in row])}")
        print(f"{' '.join(row)}")

def isWinnerFound(gameBoard, r, c, P) : 
    # check horizontally 
    if all(gameBoard[r][j] == P for j in range(3)) : 
        return True 
    
    # check vertically 
    if all(gameBoard[i][c] == P for i in range(3)) : 
        return True 
    
    # check primary diagonal 
    if r == c : 
        if all(gameBoard[i][i] == P for i in range(3)) : 
            return True 
            
    # check secondary diagonal 
    if r+c == 2: 
        if all(gameBoard[i][2-i] == P for i in range(3)) : 
            return True
    
    return False 

def isBoardFull(gameBoard) : 
    if all(gameBoard[i][j] != '-' for j in range(3) for i in range(3)) : 
        return True 
    return False 

def startsToPlay(gameBoard) : 
    P1 = 'o' 
    P2 = 'x' 
    P = True

    while True : 
        if P : 
            print("Player 1: ")
            r, c = map(int, input("Enter the row and column: ").split()) 
            if gameBoard[r][c] != '-' : 
                print("Choose another row and col.")
                continue 

            for i in range(3) : 
                for j in range(3) : 
                    if i==r and j==c : 
                        gameBoard[i][j] = 'O'             
            displayGameBoard(gameBoard)
            res = isWinnerFound(gameBoard, r, c, P1)
            if res : 
                print(f"Player P1 is won!")
                break 
            else :
                P = False 
        else : 
            print("Player 2: ")
            r, c = map(int, input("Enter the row and column: ").split()) 
            if gameBoard[r][c] != '-' : 
                print("Choose another row and col.")
                continue 
            for i in range(3) : 
                for j in range(3) : 
                    if i==r and j==c : 
                        gameBoard[i][j] = 'X' 
            displayGameBoard(gameBoard)
            res = isWinnerFound(gameBoard, r, c, P2)
            if res : 
                print(f"Player P2 is won!")
                break 
            else :
                P = True

        if isBoardFull(gameBoard) : 
            print("It's a Tie") 
            break 

def main() : 
    gameBoard = [['-' for j in range(3)] for i in range(3)] 
    print("Welcome to Tic-Tac-Toe game! Here is the initial game board and you need to select the row and column number in every move.")

    for row in gameBoard : 
        print(f"{' '.join([element for element in row])}")
    
    startsToPlay(gameBoard)

if __name__ == "__main__" : 
    main() 