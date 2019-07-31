import random

# 排序算法的核心为：比较、交换


def quick_sort(arr, low, high):
    if low >= high:
        return
    if low < high:
        q = get_position(arr, low, high)
        quick_sort(arr, low, q - 1)
        quick_sort(arr, q + 1, high)


def get_position(arr, low, high):
    left = low
    right = high
    flag = arr[low]
    while left < right:
        while arr[right] > flag and left < right:
            right = right - 1
        while arr[left] <= flag and left < right:
            left = left + 1
        if left < right:
            arr[left], arr[right] = arr[right], arr[left]
    arr[low] = arr[right]
    arr[right] = flag
    return right


def quick_sort_20190703(arr, start, end):
    if start >= end:
        return          # 定义出口
    flag = arr[start]   # 选择标志位
    left = start
    right = end
    while left < right:
        while left < right and arr[right] > flag:   # 移动右指针
            right -= 1
        while left < right and arr[left] <= flag:   # 移动左指针
            left += 1
        if left < right:
            arr[left], arr[right] = arr[right], arr[left]   # 交换左右指针对应数据
    arr[start], arr[right] = arr[right], arr[start]     # 这步很关键，将标志位放到正确的位置
    quick_sort_20190703(arr, start, right - 1)
    quick_sort_20190703(arr, right + 1, end)


if __name__ == '__main__':
    arr = []
    list(map(lambda x: arr.append(random.randint(0, 100)), range(10)))
    print(arr)
    # quick_sort(arr, 0, 9)
    quick_sort_20190703(arr, 0, 9)
    print(arr)
