#Create a python program the creates a checkerboard pattern as shown.
#You should prompt for the size of the board (minus the frame).
#Create the checkerboard within a 2D array and print it out. Your solution should work for mulitple sizes.
#Hints:
    #Prompt to the size of the board (n)
    #Create an empty 2D List
    #Append the top of the board, consisting of an plus sign, n dashes, and a plus sign
    #For n times, append interior rows, consisting of a vertical bar, n spaces, and a vertical bar
    #Append the bottom of the board, consisting of an plus sign, n dashes, and a plus sign
    #Loop through the interior rows and columns; set the element to an asterisk if the column and row index are even/odd or odd/event
    #Loop through the entire board and and print the values.

# Prompt for size
n = int(input("Enter Size: "))

# Create empty 2D list (board)
board = []

# Top border
board.append(["+"] + ["-"] * n + ["+"])

# Middle rows
for i in range(n):
    row = ["|"] + [" "] * n + ["|"]
    board.append(row)

# Bottom border
board.append(["+"] + ["-"] * n + ["+"])

# Fill checkerboard pattern
for i in range(1, n + 1):
    for j in range(1, n + 1):
        # Checkerboard rule: (i + j) is even
        if (i + j) % 2 == 0:
            board[i][j] = "*"

# Print board
for i in range(len(board)):
    for j in range(len(board[i])):
        print(board[i][j], end="")
    print()