##############################
# Pair Programming Wk4 Prob3
##############################

grid = [
        [" ", " ", "M", "M", " "],
        ["M", " ", " ", "M", " "],
        [" ", " ", " ", " ", " "],
        [" ", "M", " ", " ", "M"],
        [" ", "M", "M", "M", " "]
       ]

def click(board, row, col):
    """Output of clicking on a space.

    Should return -1 if a mine was hit, otherwise the number of surrounding mines.

    Inputs:
        board (list of list of str): The state of the board, with "M" for mines
        row (int): the row index to simulate clicking
        col (int): the column index to simulate clicking
    Outputs:
        (int): The number of surrounding mines or -1 for a direct hit
    """
    pass # Add your code below and remove this pass!








if __name__ == '__main__':
    print(click(grid, 1, 3))
    print(click(grid, 1, 2))
    print(click(grid, 4, 4))

