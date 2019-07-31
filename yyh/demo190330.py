from math import ceil


def chunk(lst, size):
    return list(
        map(lambda x: lst[x * size:(x + 1) * size],
            list(range(0, ceil(len(lst) / size)))))


ls = [1, 2, 3, 4]

print(chunk(ls, 3))

print(ls[1:9])

print(list(range(5))[::-1])

a = list(map(str, range(9)))
print()

print(((5^-90)>>27)^1)
import sys
print(sys.getsizeof(5))
a = 5
print(a.__sizeof__())