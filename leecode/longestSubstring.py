
def longest_substring(s):
    sub_str = []
    if len(s) < 2:
        return len(s)
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            if s[j] in s[i:j]:
                sub_str.append(s[i:j])
                break
            if j == len(s) - 1:
                if s[j] in s[i:j]:
                    sub_str.append(s[i:j])
                else:
                    sub_str.append(s[i:j+1])
    print(sub_str)
    ls = ""
    for i in sub_str:
        if len(i) > len(ls):
            ls = i
    print(ls)


def sliding_window(s):
    l = 0
    r = 0
    sub_str = ""
    # for l in range(len(s)):
    while True:
        pass
        



if __name__ == '__main__':
    longest_substring("ababcdab")
