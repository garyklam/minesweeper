import unittest
from inputgen import InputGenerator
from officialsolution import Minesweeper


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
    unittest.main()
