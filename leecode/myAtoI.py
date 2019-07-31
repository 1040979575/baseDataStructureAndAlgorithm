'''
请你来实现一个 atoi 函数，使其能将字符串转换成整数。

首先，该函数会根据需要丢弃无用的开头空格字符，直到寻找到第一个非空格的字符为止。

当我们寻找到的第一个非空字符为正或者负号时，则将该符号与之后面尽可能多的连续数字组合起来，作为该整数的正负号；假如第一个非空字符是数字，则直接将其与之后连续的数字字符组合起来，形成整数。

该字符串除了有效的整数部分之后也可能会存在多余的字符，这些字符可以被忽略，它们对于函数不应该造成影响。

注意：假如该字符串中的第一个非空格字符不是一个有效整数字符、字符串为空或字符串仅包含空白字符时，则你的函数不需要进行转换。

在任何情况下，若函数不能进行有效的转换时，请返回 0

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/string-to-integer-atoi
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# 此题看似简单，但是需要考虑多种异常情况和边界情况，算法复杂度上面倒没有什么要求
# 看了题解，觉得思路开阔，个人人为最佳解法为正则表达式
# 以此类推，应对查找特定子串的问题，都可考虑正则，特别是要求特别多的时候
# 个人初始想法为双指针，标记子串起始与末尾


def atoi(ss):
    start = 0
    end = 0
    for i in range(len(ss)):
        if ss[i] in list(map(str, range(0, 9))) or ss[i] in ['+', '-']:
            start = i
            break
    for j in range(start + 1, len(ss)):
        if ss[j] not in list(map(str, range(0, 9))):
            end = j
            break
    if end != 0:
        if ss[start] in ['+', '-']:
            if end > start:
                return ss[start:end + 1]
        else:
            return ss[start:end + 1]
    return 0

# 正则表达式：(+/-)[0-9]+


if __name__ == "__main__":
    print(atoi("45"))
    import re
    '''re.findall("(+/-)[0-9]+", "45")'''
