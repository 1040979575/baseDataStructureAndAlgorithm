import random


def bubble_sort(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


if __name__ == '__main__':
    arr = []
    list(map(lambda x: arr.append(random.randint(0, 100)), range(10)))
    print(arr)
    bubble_sort(arr)
    print(arr)
