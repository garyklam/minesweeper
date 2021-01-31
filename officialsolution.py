import unittest
from inputgen import InputGenerator


class Minesweeper:
    """Takes input from file redirect and builds a string containing the minefield information. Passes this info line
    by line to a Minefield object that converts the field to the numerical representation and stores this representation
    to be returned with a __str__ method."""

    def __init__(self, file=None, manual_input=None):
        """Field count starts at 1, initializes empty string to hold the converted text form. Starts while loop to
        collect input line by line and stores it in an array called mine_text. Once a line containing 0 0, an end
        marker is added to mine_text and the loop breaks. Another loop begins that takes the first line and obtains
        field dimensions and creates a Minefield objects with those dimensions, it then passes the subsequent number
        of lines to the Minefield based on the row dimension. The Minefield is converted and saved to this class before
        moving to the next line, continuing until the end marker is reached."""
        field_num = 1
        self.string_representation = ""
        self.mine_text = []
        if file:
            handle = open(file, "r")
            self.mine_text = handle.read().split("\n")
            handle.close()
        elif manual_input:
            self.mine_text = manual_input.split("\n")
        else:
            while True:
                line = input()
                if line == "0 0":
                    self.mine_text.append(f'{line}')
                    break
                self. mine_text.append(f'{line}')
        curr_line = 0
        while True:
            line = self.mine_text[curr_line]
            if line == "0 0":
                break
            dimensions = line.split(" ")
            self.row, self.col = int(dimensions[0]), int(dimensions[1])
            if self.row*self.col > 0:
                self.start_row = curr_line + 1
                self.end_row = curr_line + self.row
                self.string_representation += f'Field #{field_num}\n'
                for i in range(self.start_row, self.end_row+1):
                    self.convert(i)
                    self.string_representation += "\n"
                field_num += 1
                curr_line = self.end_row + 1
            else:
                curr_line += 1
                continue

    def convert(self, curr):
        """Checks each cell in the 2d array, if the spot is not a mine, it calls _find_adjacent_mines to determine
        how many mines are adjacent and inserts that number into the string. If the cell is a mine, inserts a *."""
        for col in range(self.col):
            if self.mine_text[curr][col] == ".":
                mines = self._find_adjacent_mines(curr, col)
                self.string_representation += f'{mines}'
            else:
                self.string_representation += f'*'


    def _find_adjacent_mines(self, row, col):
        """Determines the indices of the cells adjacent to the cell indicated by the parameters. Checks the if each
        adjacent cell is within the bounds of the 2d array. If it is and the cell contains a mine, adds 1 to the mine
        counter. Returns the number of mines once each adjacent cell is checked."""
        mines = 0
        y_range = range(row-1, row+2)
        x_range = range(col-1, col+2)
        for y in y_range:
            for x in x_range:
                if self.end_row >= y >= self.start_row and self.col-1 >= x >= 0 and self.mine_text[y][x] == "*":
                    mines += 1
                else:
                    continue
        return mines

    def __str__(self):
        return self.string_representation


class UnitTests(unittest.TestCase):

    def test_all_mines(self):
        gen = InputGenerator((10, 5, 100))
        gen.create_input_file(file_name="test_input.txt")
        expected = "Field #1\n"
        for i in range(10):
            for j in range(5):
                expected += "*"
            expected += "\n"
        minesweeper = Minesweeper(file="test_input.txt")
        self.assertEqual(f'{minesweeper}', expected)

    def test_no_mines(self):
        gen = InputGenerator((5, 10, 0))
        gen.create_input_file(file_name="test_input.txt")
        expected = "Field #1\n"
        for i in range(5):
            for j in range(10):
                expected += "0"
            expected += "\n"
        minesweeper = Minesweeper(file="test_input.txt")
        self.assertEqual(f'{minesweeper}', expected)

    def test_max_rows(self):
        gen = InputGenerator((100, 5, 0))
        gen.create_input_file(file_name="test_input.txt")
        expected = "Field #1\n"
        for i in range(100):
            for j in range(5):
                expected += "0"
            expected += "\n"
        minesweeper = Minesweeper(file="test_input.txt")
        self.assertEqual(f'{minesweeper}', expected)

    def test_max_columns(self):
        gen = InputGenerator((5, 100, 0))
        gen.create_input_file(file_name="test_input.txt")
        expected = "Field #1\n"
        for i in range(5):
            for j in range(100):
                expected += "0"
            expected += "\n"
        minesweeper = Minesweeper(file="test_input.txt")
        self.assertEqual(f'{minesweeper}', expected)

    def test_max_rows_and_columns(self):
        gen = InputGenerator((100, 100, 0))
        gen.create_input_file(file_name="test_input.txt")
        expected = "Field #1\n"
        for i in range(100):
            for j in range(100):
                expected += "0"
            expected += "\n"
        minesweeper = Minesweeper(file="test_input.txt")
        self.assertEqual(f'{minesweeper}', expected)

    def test_one_row(self):
        gen = InputGenerator((1, 100, 0))
        gen.create_input_file(file_name="test_input.txt")
        expected = "Field #1\n"
        for i in range(1):
            for j in range(100):
                expected += "0"
            expected += "\n"
        minesweeper = Minesweeper(file="test_input.txt")
        self.assertEqual(f'{minesweeper}', expected)

    def test_one_column(self):
        gen = InputGenerator((100, 1, 0))
        gen.create_input_file(file_name="test_input.txt")
        expected = "Field #1\n"
        for i in range(100):
            for j in range(1):
                expected += "0"
            expected += "\n"
        minesweeper = Minesweeper(file="test_input.txt")
        self.assertEqual(f'{minesweeper}', expected)

    def test_zero_rows(self):
        gen = InputGenerator((0, 10))
        gen.create_input_file(file_name="test_input.txt")
        expected = ""
        minesweeper = Minesweeper(file="test_input.txt")
        self.assertEqual(f'{minesweeper}', expected)

    def test_zero_cols(self):
        gen = InputGenerator((10, 0))
        gen.create_input_file(file_name="test_input.txt")
        expected = ""
        minesweeper = Minesweeper(file="test_input.txt")
        self.assertEqual(f'{minesweeper}', expected)

    def test_zero_cols_and_zero_rows(self):
        gen = InputGenerator((0, 0))
        gen.create_input_file(file_name="test_input.txt")
        expected = ""
        minesweeper = Minesweeper(file="test_input.txt")
        self.assertEqual(f'{minesweeper}', expected)

    def test_empty_field_at_start(self):
        gen = InputGenerator((0, 5), (2, 4, 0), (4, 2, 100))
        gen.create_input_file(file_name="test_input.txt")
        expected = "Field #1\n"
        for i in range(2):
            for j in range(4):
                expected += "0"
            expected += "\n"
        expected += "Field #2\n"
        for i in range(4):
            for j in range(2):
                expected += "*"
            expected += "\n"
        minesweeper = Minesweeper(file="test_input.txt")
        self.assertEqual(f'{minesweeper}', expected)

    def test_empty_field_in_middle(self):
        gen = InputGenerator((2, 4, 0), (0, 5), (4, 2, 100))
        gen.create_input_file(file_name="test_input.txt")
        expected = "Field #1\n"
        for i in range(2):
            for j in range(4):
                expected += "0"
            expected += "\n"
        expected += "Field #2\n"
        for i in range(4):
            for j in range(2):
                expected += "*"
            expected += "\n"
        minesweeper = Minesweeper(file="test_input.txt")
        self.assertEqual(f'{minesweeper}', expected)

    def test_empty_field_at_end(self):
        gen = InputGenerator((2, 4, 0), (4, 2, 100), (0, 5))
        gen.create_input_file(file_name="test_input.txt")
        expected = "Field #1\n"
        for i in range(2):
            for j in range(4):
                expected += "0"
            expected += "\n"
        expected += "Field #2\n"
        for i in range(4):
            for j in range(2):
                expected += "*"
            expected += "\n"
        minesweeper = Minesweeper(file="test_input.txt")
        self.assertEqual(f'{minesweeper}', expected)

    def test_generic_two_by_two(self):
        input = "2 2\n" \
                ".*\n" \
                "*.\n" \
                "0 0"
        expected = "Field #1\n2*\n*2\n"
        minesweeper = Minesweeper(manual_input=input)
        self.assertEqual(f'{minesweeper}', expected)

    def test_generic_three_by_three(self):
        input = "3 3\n" \
                "..*\n" \
                "..*\n" \
                "..*\n" \
                "0 0"
        expected = "Field #1\n" \
                   "02*\n" \
                   "03*\n" \
                   "02*\n"
        minesweeper = Minesweeper(manual_input=input)
        self.assertEqual(f'{minesweeper}', expected)

    def test_generic_four_by_four(self):
        input = "4 4\n" \
                "..*.\n" \
                "...*\n" \
                "**..\n" \
                "..*.\n" \
                "0 0"
        expected = "Field #1\n" \
                   "01*2\n" \
                   "233*\n" \
                   "**32\n" \
                   "23*1\n"
        minesweeper = Minesweeper(manual_input=input)
        self.assertEqual(f'{minesweeper}', expected)

    def test_generic_five_by_five(self):
        input = "5 5\n" \
                "*.**.\n" \
                "..***\n" \
                "***.*\n" \
                "***.*\n" \
                "....*\n" \
                "0 0"

        expected = "Field #1\n" \
                   "*3**3\n" \
                   "36***\n" \
                   "***7*\n" \
                   "***5*\n" \
                   "2323*\n"
        minesweeper = Minesweeper(manual_input=input)
        self.assertEqual(f'{minesweeper}', expected)

    def test_generic_multi_field(self):
        input = "4 4\n" \
                "..*.\n" \
                "...*\n" \
                "**..\n" \
                "..*.\n" \
                "2 2\n" \
                ".*\n" \
                "*.\n" \
                "3 3\n" \
                "..*\n" \
                "..*\n" \
                "..*\n" \
                "5 5\n" \
                "*.**.\n" \
                "..***\n" \
                "***.*\n" \
                "***.*\n" \
                "....*\n" \
                "0 0"
        expected = "Field #1\n" \
                   "01*2\n" \
                   "233*\n" \
                   "**32\n" \
                   "23*1\n" \
                   "Field #2\n" \
                   "2*\n" \
                   "*2\n" \
                   "Field #3\n" \
                   "02*\n" \
                   "03*\n" \
                   "02*\n" \
                   "Field #4\n" \
                   "*3**3\n" \
                   "36***\n" \
                   "***7*\n" \
                   "***5*\n" \
                   "2323*\n"
        minesweeper = Minesweeper(manual_input=input)
        self.assertEqual(f'{minesweeper}', expected)


if __name__ == '__main__':
    test = Minesweeper()
    print(test)
    # unittest.main()