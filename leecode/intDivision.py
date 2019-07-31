
'''
给定两个整数，被除数 dividend 和除数 divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。

返回被除数 dividend 除以除数 divisor 得到的商

链接：https://leetcode-cn.com/problems/divide-two-integers
'''

# 该题看起来也不难，但是其中坑很多，想要写出健壮的代码并不容易
# 我个人思考可以考虑使用上下界，不断缩小范围来确定
def division(dividend, divisor):
    temp = 0
    for i in range(dividend + 1):
        temp += abs(divisor)
        if temp > abs(dividend):
            if ((dividend ^ divisor) >> divisor.__sizeof__())^1 > 0:
                return i
            else :
                return -i
    return 2**31 - 1


def division_v2(dividend, divisor):
    def get_add_num(num, times):
        sum = 0
        for i in range(times):
            sum += num
        return sum
    low = 0
    up = dividend
    while low < up:
        mid = round((low + up) / 2)
        if get_add_num(divisor, mid) < dividend:
            low = mid
        else:
            up = mid
    return mid


if __name__ == '__main__':
    # print(division(2147483647, 1))
    print(division_v2(3, 1))
