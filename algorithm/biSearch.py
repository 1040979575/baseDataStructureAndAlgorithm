import random

# 二分查找


def bi_sarch(arr, k):
    low = 0
    high = len(arr) - 1
    arr.sort()
    while low < high:
        mid = int((low + high) >> 1) # 移位操作提高效率，对于2的乘除法都可以用位操作代替
        if arr[mid] < k:
            low = mid
        elif arr[mid] > k:
            high = mid
        else:
            return mid


if __name__ == '__main__':
    arr = []
    list(map(lambda x: arr.append(random.randint(0, 100)), range(10)))
    print(arr)
    print(arr[5])
    print(bi_sarch(arr, arr[5]))
    print(arr)
