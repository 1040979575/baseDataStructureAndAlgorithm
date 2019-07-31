'''
你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，
影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，
如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报装置的情况下，能够偷窃到的最高金额。

示例 1:

输入: [1,2,3,1]
输出: 4
解释: 偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
     偷窃到的最高金额 = 1 + 3 = 4
'''


def dp(arr):
    temp = []
    for i in range(arr.__len__()):
        if i == 0:
            temp.append(arr[i])
        elif i == 1:
            temp.append(max(arr[0], arr[1]))
        else:
            temp.append(max(temp[i - 1], arr[i] + temp[i - 2]))
    return max(temp)


if __name__ == '__main__':
    print(dp([2, 7, 9, 3, 1]))
