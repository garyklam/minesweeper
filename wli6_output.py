
#Wenqian Li net ID: wli6
def minesweeper():
    # 1 read all lines from txt.file and store them in a list of string

    with open("minesweeper_input.txt") as filename:
        lines = filename.readlines()
    # remove whitespace characters like `\n` at the end of each line

    lines = [x.strip() for x in lines]
    # initialize map_row and map_column for the mine map, update map_row and map_column for each mine map
    map_row = 0
    map_column = 0
    field = 0
    # 2 iterate through each line
    # initialize i and j for the mine map
    i = 0
    j = 0
    for i in range(len(lines)):

        row_str = lines[i]
        # 3 check if this line is number of mine map
        if row_str[0].isdigit():
            nums = row_str.split(" ")
            map_row = int(nums[0])
            map_row_start = i + 1
            map_row_end = map_row_start + map_row
            map_column = int(nums[1])
            if map_row == 0 and map_column == 0:
                return
            else:
                field += 1
                print(f"\nField#{field}:")
        else:
            # this line contains mine info, calculate mine count for each location
            # iterate through each location in str
            mine_counts = ''
            for j in range(map_column):
                # if it's mine, just add it to the mine_counts output string
                if row_str[j] == '*':
                    mine_counts = mine_counts + row_str[j]
                else:
                    directions = [(-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0)]
                    mine_count = 0
                    for d in directions:
                        new_i, new_j = i + d[0], j + d[1]
                        if map_row_start <= new_i < map_row_end and 0 <= new_j < map_column and lines[new_i][new_j] == '*':
                            mine_count += 1
                    mine_counts = mine_counts + str(mine_count)
            print(mine_counts)

minesweeper()
