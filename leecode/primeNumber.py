#题目：求出大于或等于 N 的最小回文素数
#该题看似简单，若想追求效率，则需要从素数方面考虑，借用数学方法优化

import datetime


def is_huiWen(num):
    ss = str(num)
    # for i in range(int(len(ss)/2)):
        # if ss[i] != ss[len(ss) - i -1]:

    if ss != ss[::-1]:  # 巧用切片，秒杀回文
            return False
    return True


def is_prime(num):
    for i in range(2, int(num/2)):
        if int(num) % i == 0:
            return False
    return True


if __name__ == '__main__':
    start = datetime.datetime.now()
    num = int(input("input a number: "))
    while True:
        if is_prime(num) and is_huiWen(num):
            print(num)
            break
        else:
            num += 1

    print(datetime.datetime.now() - start)

