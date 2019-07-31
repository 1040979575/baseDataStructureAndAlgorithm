
PRECISION = 0.0001


def get_sqrt(num):
    low = num - 1
    high = num + 1
    sum = 1
    while True:
        if sum * sum < num:
            sum += 1

def maxAbsValExpr(self, arr1, arr2):
    sum = 0
    for i in list(range(len(arr1))):
        for j in list(range(len(arr1))):
            if i != j:
                max(sum, abs(arr1[i] - arr1[j]) + abs(arr2[i] - arr2[j]) + abs(i - j))

    return sum


if __name__ == '__main__':
    print()