

def queensAttack(n, k, r_q, c_q, obstacles):
    top_left = (-1, -1)
    top_right = (n+1, -1)
    bot_left = (n+1,  n+1)
    bot_right = (n+1, n+1)
    r_low = -1
    r_high = n+1
    c_low = -1
    c_high = n+1

    slope = r_q - c_q

    for i in range(len(obstacles)):
        row, column = obstacles[i]

        if column == c_q and row < r_q and row > r_low: r_low = row
        else:
            if column == c_q and row > r_q and row < r_high: r_high = row

        if row == r_q and column < c_q and column > c_low: c_low = column
        else:
            if row == r_q and column < c_q and column < c_high: c_high = column

        # Top Left to Bottom Right slope
        if (row - column) == slope:
            if row > top_left[0] and row < r_q and column < top_left[0] and column < c_q:
                top_left = (row,column)
            else:
                if row < bot_right[0] and row > r_q:
                    bot_right = (row,column)


        # Top Right Block
        if r_q - row == column - c_q and row < r_q and column > c_q and row > top_right[0] and top_right[1] > column:
            top_right = (row, column)

        #Bottom Left Block
        if row - r_q == c_q - column and row > r_q and column < c_q and row < bot_left[0] and column > bot_left[1]:
            bot_left = (row, column)


    count = 0
    if r_low == -1:
        count += (r_q - 1)
    else:
        count += (r_q - r_low - 1)

    if r_high == (n+1):
        count += (n - r_q)
    else:
        count += (r_high - r_q - 1)

    # Columns
    if c_low == -1:
        count += (c_q - 1)
    else:
        count += (c_q - c_low - 1)

    if c_high == (n+1):
        count += (n - c_q)
    else:
        count += (c_high - c_q - 1)

    # Top left - bot right diagonal
    if top_left == (-1, -1):
        if r_q <= c_q: count += (r_q - 1)
        else: count += (c_q - 1)
    else:
        count += (r_q - top_left[0] - 1)

    if bot_right == (n+1, n+1):
        if r_q >= c_q: count += (n - r_q)
        else: count += (n - c_q)
    else:
        count += (bot_right[0] - r_q - 1)

    if bot_left == (n+1,n+1):
        if (n - r_q) <= c_q: count += (n - r_q)
        else: count += (c_q - 1)
    else:
        count += (r_q - bot_left[0] - 1)

    if top_right == (n + 1, -1):
        if r_q <= (n - c_q): count += (r_q - 1)
        else: count += (n - c_q)
    else:
        count += (r_q - top_right[0])

    return count

n = 5
k = 3
r_q = 4
c_q = 3
obstacles = [(5,5), (4,2), (2,3)]
queensAttack(n,k, r_q, c_q, obstacles)
