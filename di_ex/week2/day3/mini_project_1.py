# Instructions:
# Tic Tac Toe is played on a 3x3 grid. Players take turns marking empty squares with their symbol
# (‘O’ or ‘X’). The first player to get three of their symbols in a row (horizontally, vertically, or
# diagonally) wins. If all squares are filled and no player has three in a row, the game is a tie.


# Step 1: Representing the Game Board

# You’ll need a way to represent the 3x3 grid.
# A list of lists (a 2D list) is a good choice.
# Initially, each cell in the grid should be empty (e.g., represented by a space ‘ ‘).


def display_board(board):

    drawing = f"""{"-"*7}\n|{"|".join(board[0])}|\n{"-"*7}\n|{"|".join(board[1])}|\n{"-"*7}\n|{"|".join(board[2])}|\n{"-"*7}\n"""

    return drawing


def player_input(player, board):
    flag = False
    while flag == False:
        position = input(
            f"{player[0]} please enter a row and a column in numbers, separated by a comma\n"
        ).split(",")
        try:
            row = int(position[0]) - 1
            col = int(position[1]) - 1
            if row in range(3) and col in range(3):
                if board[row][col] == " ":
                    board[row][col] = player[1]
                    flag = True
                    return board
                else:
                    print("That position is taken! Try again")
                    return board
            else:
                print("You did not enter a valid position")

        except ValueError as ve:
            print("You did not enter a valid position")


def check_win(board, player):
    check_row = ""
    for i in range(len(board)):
        check_row = "".join(board[i])
        if check_row == f"{3*player[1]}":
            print(f"{player[0]} - You won")
            return True
        check_column = "".join([board[j][i] for j in range(len(board))])
        if check_column == f"{3*player[1]}":
            print(f"{player[0]} - You won")
            return True
    check_diagonal_1 = "".join([board[i][i] for i in range(len(board))])
    check_diagonal_2 = "".join(
        [board[len(board) - 1 - i][i] for i in range(len(board))]
    )
    if check_diagonal_1 == f"{3*player[1]}" or check_diagonal_2 == f"{3*player[1]}":
        print(f"{player[0]} - You won")
        return True
    return False


def check_tie(board):
    board_string = ""
    for i in board:
        board_string += "".join(i)
    if board_string.isalpha():
        print("It's a Tie")
        return True
    else:
        return False


def play():

    board = []
    for i in range(3):
        board.append([])
        for j in range(3):
            board[i].append(" ")

    print(display_board(board))

    player1 = (input("Please enter player 1 name\n"), "x")
    player2 = (input("Please enter player 2 name\n"), "o")

    game_over = False
    while game_over == False:

        if check_win(board, player2) == False:
            player_input(player1, board)
            print(display_board(board))
            if check_win(board, player1) == False:
                player_input(player2, board)
                print(display_board(board))
            else:
                game_over = True
        else:
            game_over = True
        if check_tie(board) == True:
            game_over = True


play()

# Step 2: Displaying the Game Board

# Create a function called display_board() to print the current state of the game board.
# The output should visually represent the 3x3 grid.
# Think about how to format the output to make it easy to read.


# Step 3: Getting Player Input

# Create a function called player_input(player) to get the player’s move.
# The function should ask the player to enter a position (e.g., row and column numbers).
# Validate the input to ensure it’s within the valid range and that the chosen cell is empty.
# Think about how to ask the user for input, and how to validate that input.


# Step 4: Checking for a Winner

# Create a function called check_win(board, player) to check if the current player has won.
# The function should check all possible winning combinations (rows, columns, diagonals).
# If a player has won, return True; otherwise, return False.
# Think about how to check every possible winning combination.


# Step 5: Checking for a Tie

# Create a function to check if the game has resulted in a tie.
# The function should check if all positions of the board are full, without a winner.


# Step 6: The Main Game Loop

# Create a function called play() to manage the game flow.
# Initialize the game board.
# Use a while loop to continue the game until there’s a winner or a tie.
# Inside the loop:
# Display the board.
# Get the current player’s input.
# Update the board with the player’s move.
# Check for a winner.
# Check for a tie.
# Switch to the next player.
# After the loop ends, display the final result (winner or tie).


# Tips:

# Consider creating helper functions to break down the logic into smaller, manageable parts.
# Follow the single responsibility principle: each function should do one thing and do it well.
# Think about how to switch between players.
# Think about how you will store the player’s symbol.
