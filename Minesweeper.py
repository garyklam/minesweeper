#Net ID = pragyad.
# class minesweeper creats minesweeper layout.Locates mine at randomly genrated locations.Shows count on mine in neighbour
#in output.


import random

class minesweeper:

        #prints mine layout.
        def print_mines_layout(self,array):
              for a in array:
                  for elem in a:
                    print("{}".format(elem).rjust(2), end="") #removes brackets and comma from array.
                  print(end="\n")

        #randomly selects mine no. and set mine at randomly selected locations.
        def set_mines(self,array,row,col):
            mine_no = random.randint(1, (row))
            count = 0
            while count < mine_no:
                    r = random.randint(0,row-1)
                    c=random.randint(0,col-1)
                    if array[r][c]!='*':
                       array[r][c]='*'
                       count+=1
            return array

        def calculate_neighbour(self,array,row,column):
            # Loop for counting each cell value

           for r in range(row):
                for col in range(column):
                    # Skip, if it contains a mine
                    if array[r][col] == '*':
                        continue
                    # Check up
                    if r > 0 and array[r - 1][col] == '*':
                        if isinstance(array[r][col],int):
                            array[r][col] = array[r][col] + 1
                        else:
                            array[r][col] = 1
                    # Check down
                    if r <row - 1 and array[r + 1][col] == '*':
                        if isinstance(array[r][col], int):
                            array[r][col] = array[r][col] + 1
                        else:
                            array[r][col] = 1
                    # Check left
                    if col > 0 and array[r][col - 1] == '*':
                        if isinstance(array[r][col], int):
                            array[r][col] = array[r][col] + 1
                        else:
                            array[r][col] = 1
                    # Check right
                    if col < row - 1 and array[r][col + 1] == '*':
                        if isinstance(array[r][col], int):
                            array[r][col] = array[r][col] + 1
                        else:
                            array[r][col] = 1
                    # Check top-left
                    if r > 0 and col > 0 and array[r - 1][col - 1] == '*':
                        if isinstance(array[r][col], int):
                            array[r][col] = array[r][col] + 1
                        else:
                            array[r][col] = 1
                    # Check top-right
                    if r > 0 and col < row - 1 and array[r - 1][col + 1] == '*':
                        if isinstance(array[r][col], int):
                            array[r][col] = array[r][col] + 1
                        else:
                            array[r][col] = 1
                    # Check below-left
                    if r < row - 1 and col > 0 and array[r + 1][col - 1] == '*':
                        if isinstance(array[r][col], int):
                            array[r][col] = array[r][col] + 1
                        else:
                            array[r][col] = 1
                    # Check below-right
                    if r < row - 1 and col < row - 1 and array[r + 1][col + 1] == '*':
                        if isinstance(array[r][col], int):
                            array[r][col] = array[r][col] + 1
                        else:
                            array[r][col] = 1
                    #if no * in neighbour make count zero.
                    if array[r][col]=='.':
                        array[r][col] = 0

           return array

if __name__ == '__main__':
    test = minesweeper()
    print(test)

    inputarray=[]
    while 1:
        # Input from the user
        inp = input(" ").split()
        # Standard input
        if len(inp) == 2:
        # Try block to handle errant input
            try:
                val = list(map(int, inp))
            except ValueError:
                    print("Wrong input!")
                    break
        m=int(inp[0])
        n=int(inp[1])
        if (m>0 and m<= 100) or (n>0 and n<=100):
            array=[['.' for i in range(n)] for j in range(m)]
            test.print_mines_layout(test.set_mines(array,m,n))
            inputarray.append(test.calculate_neighbour(array,m,n))
        else:
            break
    count=1
    for x in inputarray:
            print('Field #',count,':')
            test.print_mines_layout(x)
            count +=1





