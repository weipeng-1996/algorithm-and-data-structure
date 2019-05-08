

def reverse(x):
    if x == 0:
        return 0
    s = str(x)
    l = len(s)
    if s[l-1] == '0':
        s = s[:l-1]
    if s[0] == '-':
        s = '-' + s[-1:0:-1]
    else:
        s = s[::-1]
    return int(s)


if __name__ == '__main__':
    num = int(input())
    print(reverse(num))