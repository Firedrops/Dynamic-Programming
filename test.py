import sys

def canSumNaive(targetSum, inputs):
    if targetSum == 0:
        return True
    elif targetSum < 0:
        return False

    for num in inputs:
        return num


if __name__ == '__main__':
    sys.stdout.write(canSumNaive(7, [2, 3, 4]))
