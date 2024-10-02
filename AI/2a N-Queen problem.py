print("04_Jayprabha Nadar")

class QueenChessBoard:
    def __init__(self, size):
        # Board has dimensions size x size
        self.size = size
        # columns[r] is a number c if a queen is placed at row r and column c.
        self.columns = []

    def place_in_next_row(self, column):
        self.columns.append(column)

    def remove_in_current_row(self):
        return self.columns.pop()

    def is_this_column_safe_in_next_row(self, column):
        row = len(self.columns)  # Index of the next row
        
        # Check if the column is safe (column and diagonals)
        for queen_row, queen_column in enumerate(self.columns):
            if column == queen_column:  # Same column
                return False
            if queen_column - queen_row == column - row:  # Same diagonal
                return False
            if queen_column + queen_row == column + row:  # Same other diagonal
                return False
        return True

    def display(self):
        # Display the board with 'Q' for queen and '.' for empty spaces
        for row in range(self.size):
            for column in range(self.size):
                if column == self.columns[row]:
                    print('Q', end=' ')
                else:
                    print('.', end=' ')
            print()


def solve_queen(size):
    """
    Display a chessboard for each possible configuration of placing n
    queens on an n x n chessboard and print the number of such
    configurations.
    """
    board = QueenChessBoard(size)
    number_of_solutions = 0
    row = 0
    column = 0

    # Iterate over rows of the board
    while True:
        # Place queen in next row
        while column < size:
            if board.is_this_column_safe_in_next_row(column):
                board.place_in_next_row(column)
                row += 1
                column = 0
                break
            else:
                column += 1

        # If no column found, or if the board is full
        if column == size or row == size:
            # If the board is full, we have found a solution
            if row == size:
                board.display()  # Display the solution
                print()
                number_of_solutions += 1

                # Backtrack by removing the queen from the last row
                board.remove_in_current_row()
                row -= 1

            # Now backtrack
            try:
                prev_column = board.remove_in_current_row()
            except IndexError:
                # All queens removed, thus no more configurations
                break

            # Try the previous row again, start checking at column = (1 + prev_column)
            row -= 1
            column = 1 + prev_column

    print('Number of solutions:', number_of_solutions)


# Get the size of the board from the user
n = int(input('Enter n: '))
solve_queen(n)
