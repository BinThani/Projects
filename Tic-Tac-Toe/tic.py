#TODO Need to check for tie

def Userprompt():
    for_Tic = True

    #display()

    while for_Tic:
        try:
            X, Y = int(input("Y Coordinate: ")), int(input("X Coordinate: "))
        except ValueError:
            print("Wrong Values.\n")
            # Bad Input from The user...
            continue
        # Check's For High values.
        if X > 2 or X < 0:
            print("Wrong Coordinates Try again.")
            continue
        if Y > 2 or Y < 0:
            print("Wrong Coordinates Try again.")
            continue
        else:
            break
    return X, Y


def display():
    global Tic_Display
    count = 0
    Tic_Display = [["", "", ""],
                   ["", "", ""],
                   ["", "", ""]]

    print(f"    {0}    {1}    {2}")
    for i in Tic_Display:
        print(f"{count} {i}")
        count += 1
    return Tic_Display


def add(X, Y, Board, Turn):
    # Returns True if successful.
    if not Board[X][Y]:
        Board[X][Y] = Turn
        return True
    else:
        return "There is a value Already."

def checker(X, Y, board):
    """
    Check's if user added value to
    Empty Strings.
    """
    if board[X][Y] == "":
        return False
    print("Already Placed value...")
    return True

def winner(playerX, playerO):
    if playerX:
        print("X Wins")
    pass

def winning_board(board):

    if ((board[0][0] == board[1][0] == board[2][0] == "X") or
            (board[0][1] == board[1][1] == board[2][1] == "X") or
            (board[0][2] == board[1][2] == board[2][2] == "X") or
            (board[0][0] == board[0][1] == board[0][2] == "X") or
            (board[1][0] == board[1][1] == board[1][2] == "X") or
            (board[2][0] == board[2][1] == board[2][2] == "X") or
            (board[0][0] == board[1][1] == board[2][2] == "X") or
            (board[0][2] == board[1][1] == board[2][0] == "X")):

        playerX = True
        playerO = False

        return playerX, playerO

    elif ((board[0][0] == board[1][0] == board[2][0] == "O") or
        (board[0][1] == board[1][1] == board[2][1] == "O") or
        (board[0][2] == board[1][2] == board[2][2] == "O") or
        (board[0][0] == board[0][1] == board[0][2] == "O") or
        (board[1][0] == board[1][1] == board[1][2] == "O") or
        (board[2][0] == board[2][1] == board[2][2] == "O") or
        (board[0][0] == board[1][1] == board[2][2] == "O") or
            (board[0][2] == board[1][1] == board[2][0] == "O")):

        playerX = False
        playerO = True

        return playerX, playerO

    else:
        playerX = False
        playerO = False
        return playerX, playerO


if __name__ == '__main__':
    board = display()
    X_Turn = 0
    O_Turn = 0
    while board:
        X, Y = Userprompt()
        if checker(X, Y, board):
            continue
        if X_Turn == O_Turn:
            print("X's Turn\n")
            result = add(X, Y, board, "X")
            O_Turn += 1
        else:
            print("O's Turn\n")
            X_Turn += 1
            result = add(X, Y, board, "O")
            # board = display()

        print(f"{0}   {1}    {2}")
        for i in board:
            print(i)
        print("\n")

        playerX, playerO = winning_board(board)
        #winner(playerX, playerO)

        if playerX:
            print("X Wins!")
            break
        elif playerO:
            print("O Wins!")
            break
