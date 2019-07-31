'''
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和
示例:
输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6
'''

# 一维变换dp
def dp(arr):
    temp = []
    for i in range(arr.__len__()):
        if i == 0:
            temp.append(arr[i])
        else:
            temp.append(max(temp[i - 1] + arr[i], arr[i]))
    return max(temp)


if __name__ == '__main__':
    print(dp([-2,1,-3,4,-1,2,1,-5,4]))