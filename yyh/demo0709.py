# -*- coding: UTF-8 -*-
import sys

def greet(name):
    print("hello" + name)


def get_sum(nums, target):
    size = len(nums)
    for i in range(0, size):
        for j in range(i + 1, size):
            if nums[i] + nums[j] == target:
                return (i, j)
    return (-1, -1)


def twoSum(nums, target):
    assert (len(nums) > 1)
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return [-1, -1]


if __name__ == '__main__':
    # print("hello world")
    # print("周五")
    # print(sys.version)
    # print(sys.version_info)
    print(get_sum([3, 1, 2, 4], 6))
    print(twoSum([3, 1, 2, 4], 6))
    aa = list(range(4))
    print(aa)