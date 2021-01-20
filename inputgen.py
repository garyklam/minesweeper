from random import choices

class InputGenerator:

    def __init__(self):
        self.minefields = ""

    def insert(self, *args):
        for field in args:
            self._convert_field(field)

    def _convert_field(self, parameters):
        x = int(parameters[0])
        y = int(parameters[1])
        try:
            minechance = int(parameters[2])
        except IndexError:
            minechance = 10

        self.minefields += f'{x} {y} \n'
        for i in range(0, x):
            for j in range(0, y):
                input = choices((".","*"), (100-minechance, minechance))
                self.minefields += input[0]
            self.minefields += "\n"

    def clear(self):
        self.minefields = ""

    def print(self):
        return self.minefields

    def create_input_file(self):
        input_file = open("minesweeper_input.txt", "w")
        input_file.write(self.minefields)

if __name__ == '__main__':
    test = InputGenerator()
    test.insert((3,5), (4,4), (1, 10, 100), (5, 2, 0), (0,0))
    print(test.print())
    test.create_input_file()