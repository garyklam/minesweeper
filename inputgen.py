from random import choices


class InputGenerator:
    """Class for creating input files for minesweeper project. Each minefield is defined by 3 parameters, width, length
    and chance of mine. Width and length must be defined for each field, mine chance is 10% by default and can be changed
    by adding another parameter. These parameters need to be grouped in a tuple (e.g. (3,2,15) for a field that is
    3 rows by 2 columns and a 15% chance for a mine). Multiple tuples can be included in the intizilization or with
    the insert method to create an input file with multiple minefields."""
    def __init__(self, *args):
        """
        Takes in input parameters as tuples and converts them to the text representation. Any number of fields can be
        passed in, each field requires at least two paramaters, the width and length of the field. The chance of each
        spot containing a mine is 10% unless a different percent is passed in.
        """
        self.minefields = ""
        for field in args:
            self._convert_field(field)
        self.minefields += "0 0"

    def insert(self, *args):
        """Allows additional fields to be added without creating another instance of the class."""
        for field in args:
            self._convert_field(field)

    def _convert_field(self, parameters):
        x = int(parameters[0])
        y = int(parameters[1])
        self.minefields += f'{x} {y}\n'
        if x*y == 0:
            return
        try:
            minechance = int(parameters[2])
        except IndexError:
            minechance = 10
        for i in range(0, x):
            for j in range(0, y):
                input = choices((".","*"), (100-minechance, minechance))
                self.minefields += input[0]
            self.minefields += "\n"

    def clear(self):
        self.minefields = ""

    def print(self):
        """Returns string representing the minefields, used for checking output before creating the input file."""
        return self.minefields

    def create_input_file(self, file_name=None):
        """Creates or rewrites a text file with the current set of minefield representations. The file name is
        determined by the file name arguement and is minesweeper_input.txt by default."""
        if file_name:
            input_file = open(file_name, "w")
        else:
            input_file = open("minesweeper_input.txt", "w")
        input_file.write(self.minefields)
        input_file.close()

if __name__ == '__main__':
    test = InputGenerator((3,5), (4,4), (5, 0), (0, 3), (1, 10, 100), (5, 2, 0))
    print(test.print())
    test.create_input_file()