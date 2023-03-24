# Rosendo Lugo Jr.
# Chapter 4 Programming
# Wheat and chessboard problem

# Find the number of squares the chessboard is going to have.
squares = int(input('How many squares are on a side of your chessboard? '))

# Calculate the number of total number of squares.
total_square = squares**2

# Below are the starting numbers.
row = 1
col = 1
grains = 1
total_grains = 0

# The single for loop
print('Here is with 1 for loop: ')

for num in range(1, total_square + 1):
    print(f'row {row} col {col} has {grains} grains of wheat')
    col += 1
    # the total below keeps a running count of the total amount of the grains.
    total_grains += grains
    grains *= 2
    if col > squares:
        row += 1
        col = 1

# The total output for the grains.
print(f'There are {total_grains} total grains of wheat.')
print('And now for something completely different...')

# The nested for loop.
print('Here is with nested for loops: ')

# The 2nd set of numbers to start the nested for loop.
row2 = squares
col2 = squares
grains2 = 1
total_grains2 = 0

# A loop inside another loop.
for row2 in range(1, row2 + 1):
    for col2 in range(1, col2 + 1):
        print(f'row {row2} col {col2} has {grains2} grains of wheat')

        # the total below keeps a running count of the total amount of the grains.
        total_grains2 += grains2
        grains2 *= 2
# The total output for the grains.
print(f'There are {total_grains2} total grains of wheat.')
