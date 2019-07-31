'''
给定一个编码字符串 S。为了找出解码字符串并将其写入磁带，从编码字符串中每次读取一个字符，并采取以下步骤：
如果所读的字符是字母，则将该字母写在磁带上。
如果所读的字符是数字（例如 d），则整个当前磁带总共会被重复写 d-1 次。
现在，对于给定的编码字符串 S 和索引 K，查找并返回解码字符串中的第 K 个字母

链接：https://leetcode-cn.com/problems/decoded-string-at-index
'''

# 初步想法，该题的关键在于构建解码字符串
# 暴力法 -> 果然暴力总是会让内存溢出
# 一开始也有想到不必保存完整字符串，只需要一个变量去保存即可


def decode_at_index(s, k): # 暴力法
    ss = ""
    for i in s:
        if i.isalpha():
            ss += i
        elif i.isdigit():
            ss = ss * int(i)
    return ss[k - 1]


def decode_at_index_v2(s, k):  # 官解，逆向思维法
    size = 0
    for i in s:
        if i.isalpha():
            size += 1
        elif i.isdigit():
            size = size * int(i)

    for c in reversed(s):
        #k %= size
        if (k % size) == 0 and c.isalpha():
            return c

        if c.isdigit():
            size /= int(c)
        else:
            size -= 1


def decodeAtIndex(S, K):
    size = 0
    for c in S:
        if c.isdigit():
            size *= int(c)
        else:
            size += 1

    for c in reversed(S):
        K %= size
        if K == 0 and c.isalpha():
            return c

        if c.isdigit():
            size /= int(c)
        else:
            size -= 1


if __name__ == '__main__':
    sum = decode_at_index("ixm5xmgo78", 711)
    print("暴力：" + sum)
    sum = decode_at_index_v2("ixm5xmgo78", 711)
    print("官方：" + sum)
    ss = "hello"
    print(ss * 4)
    print(decodeAtIndex("ixm5xmgo78", 711))