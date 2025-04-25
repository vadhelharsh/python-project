import numpy as np

board = np.array([
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
])

def print_board(b):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-" * 21)
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            if j == 8:
                print(b[i][j])
            else:
                print(str(b[i][j]) + " ", end="")

def is_valid(b, num, row, col):
    
    if num in b[row]:
        return False

    
    if num in b[:, col]:
        return False


    box_x = (col // 3) * 3
    box_y = (row // 3) * 3
    if num in b[box_y:box_y+3, box_x:box_x+3]:
        return False

    return True

def is_solved(b):
    return not np.any(b == 0)

def play_game():
    while not is_solved(board):
        print_board(board)
        try:
            row = int(input("Enter row (0-8): "))
            col = int(input("Enter column (0-8): "))
            num = int(input("Enter number (1-9): "))

            if board[row][col] != 0:
                print("Cell already filled. Try another.")
                continue

            if is_valid(board, num, row, col):
                board[row][col] = num
            else:
                print("Invalid move. Try again.")

        except ValueError:
            print("Invalid input. Please enter integers.")
        except IndexError:
            print("Row and column must be between 0 and 8.")
        print()

    print("Congratulations! You solved the Sudoku!")
    print_board(board)

if __name__ == "__main__":
    play_game()
