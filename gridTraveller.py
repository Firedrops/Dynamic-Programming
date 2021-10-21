# You are a traveler on 2D grid. You begin in the top-left corner and
# your goal is to travel to the bottom-right corner. You may only move
# down or right. How many unique ways can you travel each (m * n) grid?

# Base recursive case: Works but inefficient.
# O(n^2) time complexity,
# O(n) space complexity.

def gridTravelerNaive(m, n):
    if m == 1 and n == 1:
        return 1
    elif m == 0 or n == 0:
        return 0
    return gridTravelerNaive(m - 1, n) + gridTravelerNaive(m, n - 1)


# if __name__ == '__main__':
#     print(gridTravelerNaive(3, 2))
#     print(gridTravelerNaive(5, 7)) #Don't run much higher dimensions.

# Memoization
# O(m*n) time complexity,
# O(m*n) space complexity.

def gridTravelerMemo(m, n, memo={}):

    key = str(m) + ',' + str(n)

    if key in memo:
        return memo[key]

    if m == 1 and n == 1:
        return 1
    elif m == 0 or n == 0:
        return 0
    memo[key] = gridTravelerMemo(m - 1, n, memo) + gridTravelerMemo(m, n - 1, memo)
    return memo[key]


# if __name__ == '__main__':
#     print(gridTravelerMemo(3, 2))
#     print(gridTravelerMemo(5, 7))
#     print(gridTravelerMemo(20, 20))


# Tabulation DOES NOT WORK. Takes forever even for very small inputs, don't know why.
# O(m*n) time complexity,
# O(m*n) space complexity.

def gridTravelerTabu(m, n):
    #table = [[0 for i in range(m+2)] for j in range(n+2)]
    table = [[0] * (m+2) for _ in range(n+2)] # Initialize empty 2D array of dimensions (m+2) by (n+2)

    table[1][1] = 1     # Yes table indices start at 0, but this algorithm really starts at the 2nd position in each dimension :)

    print(table)
    i = 0   # To denote position in X or row
    j = 0   # To denote position in Y or column


    while i <= m:
        while j <= n:
            current = table[i][j]  # Get value in "current" position
            print("current is " + str(current))
            print("i is " + str(i))
            print("m is " + str(m))
            print("i is " + str(i))
            print("n is " + str(n))

            # Increment in Y
            table[i][j + 1] += current
            j += 1

            # Increment in X
            table[i+1][j] += current
            i += 1
            print(table)

    return table[m][n]

if __name__ == '__main__':
    print(gridTravelerTabu(4, 3))
    #print(gridTravelerTabu(5, 7))
    #print(gridTravelerTabu(20, 20))