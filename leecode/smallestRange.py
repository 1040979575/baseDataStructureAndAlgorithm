'''
给定一个整数数组 A，对于每个整数 A[i]，我们可以选择 x = -K 或是 x = K，并将 x 加到 A[i] 中。

在此过程之后，我们得到一些数组 B。

返回 B 的最大值和 B 的最小值之间可能存在的最小差值

'''

# 这个问题归根到底是个数学问题
# 

def smallest_range(arr, k):
    arr.sort()
    sum = max(arr) - min(arr)
    for i in range(arr.__len__()):
        min = abs(arr[0] + k - arr(i))


if __name__ == '__main__':

    print(smallest_range([1, 3, 6], 3))
