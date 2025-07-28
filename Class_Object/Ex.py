n = 7


rows = n - 2  # number of rows before the last row

for i in range(1, rows):
    # Left stars
    print('* ' * i, end='')

    # Spaces (gap in the middle)
    spaces = 2 * (n - i - 1) - 1
    print('  ' * spaces, end='')

    # Right stars
    print('* ' * i)

# Last row (full row of stars)
print('* ' * (2 * rows + 1))


""""n=5
*       *
* *   * *
* * * * *"""