def printBoard(board):
    separator = "--+--+--+--+--+--+--+--"
    for i in range(8):
        print(separator)
        print("|".join(board[i]))
    print(separator)


def decode(position):
    try:
        j = ord(position[0].lower()) - ord('a')
        if j < 0 or j >= 8:
            raise ValueError("invalid column")
        # invert rows (8-...) because we start from bottom left.
        i = 8 - int(position[1])
    except ValueError:
        print(f"Cannot decode position {position}. Terminating...")
        exit()
    return i, j


def main():
    board = []
    with open("game2.txt", 'r') as f:
        for i in range(8):
            line = f.readline()
            pieces = line.rstrip('\n').split("|")
            board.append(pieces)
        printBoard(board)

        # white starts
        player = "-"

        # current winner: nobody
        winner = ""

        # process remaining lines (moves)
        for line in f:
            line = line.strip()
            print(f"\nMove: {line}")
            starting, landing = line.split("-")
            istart, jstart = decode(starting)
            iland, jland = decode(landing)
            if board[istart][jstart] == "  ":
                print(f"Starting position empty. Discarding move {line}")
            elif board[istart][jstart][1] != player:
                print(f"Starting position contains an opponent's piece. Discarding move {line}")
            elif board[iland][jland][1] == player:
                print(f"Landing position contains a piece of the current player. Discarding move {line}")
            else:  # valid move
                piece = board[istart][jstart]
                # remove from start position
                board[istart][jstart] = "  "
                # empty landing spot
                if board[iland][jland] == "  ":
                    board[iland][jland] = piece
                # landing spot occupied by other player
                else:
                    # eat piece
                    board[iland][jland] = "  "
                    # iterate over adjacent squares and explode
                    for i in range(max(iland - 1, 0), min(iland + 2, 8)):
                        for j in range(max(jland - 1, 0), min(jland + 2, 8)):
                            # check winning condition
                            # note: the request does not specify what happens if both kings explode together
                            if board[i][j] == "K-":
                                winner = "-"
                            elif board[i][j] == "K+":
                                winner = "+"
                            # explode square (if not pawn)
                            if board[i][j][0] != "p":
                                board[i][j] = "  "
            # print updated board
            printBoard(board)

            # check game end condition and possibly exit
            if winner == "-":
                print("White wins!")
                exit()
            elif winner == "+":
                print("Black wins!")
                exit()

            # change player
            if player == "+":
                player = "-"
            else:
                player = "+"


main()
