def commaIT(values):
    out = ""
    for i in range(len(values) - 1):
        out = out + values[i] + ", "
    out = out + "and " + values[len(values) - 1] +"."
    return out

spam = ['apples', 'bananas', 'tofu', 'cats', 'dogs', 'rabbits']
test = commaIT(spam)
print(test)

grid = [['.','.','.','.','.','.'],
        ['.','0','0','.','.','.'],
        ['0','0','0','0','.','.'],
        ['0','0','0','0','0','.'],
        ['.','0','0','0','0','0'],
        ['0','0','0','0','0','.'],
        ['0','0','0','0','.','.'],
        ['.','0','0','.','.','.'],
        ['.','.','.','.','.','.']]

for y in range(6):
    for x in range (9):
        print(grid[x][y], end = "")
    print('\n')

