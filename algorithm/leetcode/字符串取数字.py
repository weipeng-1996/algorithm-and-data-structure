def myAtoi(s):
    if s == '':
        return 0
    s = s.strip()
    index = ''
    symbol = ''
    if s[0] == '-' or s[0] == '+':
        symbol = s[0]
        s = s[1:]
    for i in range(len(s)):
        if s[i].isdigit():
            index = i
            continue
        else:
            break
    if index == '':
        return 0
    else:
        if symbol == '':
            s = int(s[:index+1])
        else:
            s = symbol + s[:index+1]
            s = int(s)
        if s >= 2147483647:
            return 2147483647
        elif s <= -2147483648:
            return -2147483648
        else:
            return s

if __name__ == '__main__':
    s = input()
    print(myAtoi(s))