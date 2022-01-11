# Create a Battleship Game with five rows and five columns. Use the randint method from the random library to call a random number. The user gets a certain # of total_guesses to sink a certain number of total_ships battleships.

# First, we need to welcome the player:

total_guesses = 4
total_ships = 2

print("Welcome to our Battleship game!")
print(f"You will have {total_guesses} guesses to sink {total_ships} battleships.")
print("Are you ready? \n")
answer = input("Enter Y for 'yes' or N for 'no': \n").upper()

print()

if answer == "Y":
    print("Great, good luck!")
elif answer == "N":
    print("Well, it's too late now... Good luck!")
else:
    print(f"'{answer}' wasn't an option, so I will take that as a 'YES'... Good luck!"
    )

print()

# Next, we need to create our board:

from random import randint

board = []  # creates an empty list to set-up our board

for i in range(5):
    board.append(
        ["0"] * 5
    )  # appends five "0"'s per iteration to our empty board list; there are 5 total iterations since range(5)


def print_board(board):
    for row in board:  # for each row in the board
        print(
            " ".join(row)
        )  # print each row separately, and use the .join method to combine the items in each row as a string to remove the brackets and commas. Then use the space separator to join each element of each row.


print_board(board)  # displays our Battleship board!
print()

# Next, we need to randomly call coordinates for our Battleship

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board) - 1)

correct_answers = []

for i in range(total_ships):  # do this three times
    ship_row = random_row(board)
    ship_col = random_col(board)

    correct_answers.append((ship_row, ship_col)) # store the tuples in a correct_answers list for verification

print("My Secret Battleship Coordinates:")
print(correct_answers)

print()

# Retrieve guesses from user and allow them five guesses:

point = 0

for turn in range((total_guesses)):
    print(f"Turn #: {turn + 1}")
    guess_row = int(input("Guess Row: "))
    guess_col = int(input("Guess Col: "))
    print()

    user_guess = (guess_row, guess_col)

    for i in correct_answers:
        if user_guess in correct_answers:   # checks if tuple item exists in correct_answers
            board[guess_row][guess_col] = "*"
            point += 1
            print("Oh no, you got me!")
            print(f"You sank {point} of my {total_ships} battleships!")
            break
        else:
            if guess_row not in range(5) or guess_col not in range(5):
                print("That was not even in the ocean!")
                break
            elif board[guess_row][guess_col] == "X":
                print("You already guessed that one.")
                break
            else:
                print("You missed me!")
                board[guess_row][guess_col] = "X"
                break
        
    print_board(board)
    print()

    if point == total_ships:
        print("** YOU WIN!!! GAME OVER. **")
        break

    if point < total_ships and turn == (total_guesses - 1):
        print("** YOU LOSE! GAME OVER. **")