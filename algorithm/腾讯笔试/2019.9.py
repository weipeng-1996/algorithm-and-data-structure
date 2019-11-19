import sys

if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        length = int(input())
        s = input()
        if length < 11:
            print('NO')
        elif (length == 11 and s[0] == '8'):
            print('YES')
        else:
            temp = length - 11
            if s.find('8', 0, temp) > 0:
                print('YES')
            else:
                print('NO')
