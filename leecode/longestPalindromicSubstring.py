

def get_longest_str(s):
    dt = {}
    dt.__contains__()
    pass

def is_palindromic(s):
    size = len(s)
    for i in range(int(size/2)):
        if s[i] != s[size-i-1]:
            return False
    return True


if __name__ == '__main__':
    if is_palindromic("abba"):
        print("yes")