class Minefield:
    """Holds the text representation of a single minefield based. Converts this to the desired numerical representation
    when convert() is called. Returns the current state of the minefield with __str__."""
    def __init__(self, row, col, field_number):
        self.string = ""
        self.field_num = field_number
        self.row = row
        self.col = col
        self.string = f'Field #{self.field_num}:\n'
        self.field = [["." for col in range(col)] for row in range(row)]
        self.current_row = 0

    def add_row(self, string):
        """Adds the string as a new row in the 2d array of mines."""
        col = 0
        for char in string:
            self.field[self.current_row][col] = char
            col += 1
        self.current_row += 1

    def convert(self):
        """Checks each cell in the 2d array, if the spot is not a mine, it calls _find_adjacent_mines to determine
        how many mines are adjacent and inserts that number into the string. If the cell is a mine, inserts a *."""
        for row in range(self.row):
            for col in range(self.col):
                if self.field[row][col] == ".":
                    mines = self._find_adjacent_mines(row, col)
                    self.string += f'{mines}'
                else:
                    self.string += f'*'
            self.string += "\n"

    def _find_adjacent_mines(self, row, col):
        """Determines the indices of the cells adjacent to the cell indicated by the parameters. Checks the if each
        adjacent cell is within the bounds of the 2d array. If it is and the cell contains a mine, adds 1 to the mine
        counter. Returns the number of mines once each adjacent cell is checked."""
        mines = 0
        y_range = range(row-1, row+2)
        x_range = range(col-1, col+2)
        for y in y_range:
            for x in x_range:
                if self._check_bounds(y, x) and self.field[y][x] == "*":
                    mines += 1
                else:
                    continue
        return mines

    def _check_bounds(self, y, x):
        """Checks if the row and column are within the bounds of the 2d-array initialized by the constructor."""
        if self.row-1 >= y >= 0 and self.col-1 >= x >= 0:
            return True
 
    def __str__(self):
        return self.string


class Minesweeper:
    """Takes input from file redirect and builds a string containing the minefield information. Passes this info line
    by line to a Minefield object that converts the field to the numerical representation and stores this representation
    to be returned with a __str__ method."""

    def __init__(self):
        """Field count starts at 1, initializes empty string to hold the converted text form. Starts while loop to
        collect input line by line and stores it in an array called mine_text. Once a line containing 0 0, an end
        marker is added to mine_text and the loop breaks. Another loop begins that takes the first line and obtains
        field dimensions and creates a Minefield objects with those dimensions, it then passes the subsequent number
        of lines to the Minefield based on the row dimension. The Minefield is converted and saved to this class before
        moving to the next line, continuing until the end marker is reached."""
        field_num = 1
        self.string_representation = ""
        mine_text = []
        while True:
            line = input()
            if line == "0 0":
                mine_text.append("")
                break
            mine_text.append(f'{line}')
        curr_line = 0
        while True:
            line = mine_text[curr_line]
            if line == "":
                break
            dimensions = line.split(" ")
            row, col = int(dimensions[0]), int(dimensions[1])
            if row*col > 0:
                field = Minefield(row, col, field_num)
                for i in range(1, int(dimensions[0])+1):
                    field.add_row(mine_text[curr_line+i])
                field_num += 1
                field.convert()
                self.string_representation += f'{field}\n'
                curr_line += int(dimensions[0]) + 1
            else:
                curr_line += 1
                continue

    def __str__(self):
        return self.string_representation


if __name__ == '__main__':
    test = Minesweeper()
    print(test)
