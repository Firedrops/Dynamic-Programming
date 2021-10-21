# Function to calculate the nth fibonacci number.

# Base recursive case: Works but inefficient.
# O(n^2) time complexity,
# O(n) space complexity.

def fibNaive(n):
    if n <= 2:
        return 1

    else:
        return fibNaive(n-1) + fibNaive(n-2)


# if __name__ == '__main__':
#     print(fibNaive(10))
#     print(fibNaive(20)) # Do not run higher figures... computer may die

# Memoization:
# O(n) time complexity,
# O(n) space complexity.

# def fibMemo(n, memo = {}):
#     # the "memo = {}" specifies the default value when not provided. In this case, an empty object.
#     if n in memo:
#         return memo[n]
#
#     if n <= 2:
#         return 1
#
#     else:
#         memo[n] = fibMemo(n-1, memo) + fibMemo(n-2, memo)
#
#     return memo[n]
#
#
# if __name__ == '__main__':
#     print(fibMemo(10))
#     print(fibMemo(50))

# Tabulation (iterative approach):
# O(n) time complexity,
# O(n) space complexity.

def fibTabu(n):
    table = [0] * (n + 3)
    table[1] = 1
    i = 0

    while i < n:
        i += 1
        table[i+1] += table[i]
        table[i+2] += table[i]

    return table[n]


if __name__ == '__main__':
    print(fibTabu(10))
    print(fibTabu(50))