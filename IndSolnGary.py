class Minefield:
    def __init__(self, row, col, field_number):
        self.field_num = field_number
        self.row = row
        self.col = col
        self.field = [["." for col in range(col)] for row in range(row)]
        self.current_row = 0

    def add_row(self, string):
        col = 0
        for char in string:
            self.field[self.current_row][col] = char
            col += 1
        self.current_row += 1

    def convert(self):
        for row in range(self.row):
            for col in range(self.col):
                if self.field[row][col] == ".":
                    mines = self._find_adjacent_mines(row, col)
                    self.field[row][col] = mines

    def _find_adjacent_mines(self, row, col):
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
        if self.row-1 >= y >= 0 and self.col-1 >= x >= 0:
            return True
 
    def __str__(self):
        string = f'Field #{self.field_num}:\n'
        for row in self.field:
            for cell in row:
                string += str(cell)
            string += "\n"
        return string


class Minesweeper:
    def __init__(self):
        self.field_num = 1
        self.string_representation = ""
        self.build_fields()

    def build_fields(self):
        mine_text = ""
        while True:
            line = input()
            if line == "0 0":
                break
            mine_text += f'{line}\n'
        mine_text = mine_text.split("\n")
        curr_line = 0
        while True:
            line = mine_text[curr_line]
            if line == "":
                break
            dimensions = line.split(" ")
            row, col = int(dimensions[0]), int(dimensions[1])
            if row*col > 0:
                field = Minefield(row, col, self.field_num)
                for i in range(1, int(dimensions[0])+1):
                    field.add_row(mine_text[curr_line+i])
                self.field_num += 1
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
