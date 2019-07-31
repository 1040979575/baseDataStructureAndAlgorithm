import time
import datetime


def fun(n):
    if n == 1 or n == 2:
        return 1
    return fun(n-1) + fun(n-2)


start = time.time()
print(fun(45))
end = time.time()
print(end - start)


