'''
一条包含字母 A-Z 的消息通过以下方式进行了编码：

'A' -> 1
'B' -> 2
...
'Z' -> 26
给定一个只包含数字的非空字符串，请计算解码方法的总数

'''

# 第一反应：递归 但感觉效率又不够
# 可以研究一下动态规划


def numDecoding(s):# 该实现思想上没问题，但还需要对0值做处理，此处是个坑
    if len(s) < 2:
        return 1
    if len(s) == 2:
        if int(s) <= 26:
            return 2
        else:
            return 1

    if int(s[-2:]) > 26:
        return numDecoding(s[:-1])
    else:
        return numDecoding(s[:-1]) + numDecoding(s[:-2])


if __name__ == '__main__':
    ss = "226"
    print(numDecoding(ss))
