import sys


def get_new_str(str):
    up_str = []
    lw_str = []
    for i in range(len(str)):
        if str[i] == str[i].upper():
            up_str.append(str[i])
        else:
            lw_str.append(str[i])
    temp1 = ''.join(up_str)
    temp2 = ''.join(lw_str)
    return temp2 + temp1


if __name__ == '__main__':
    while True:
        str = sys.stdin.readline().strip()
        if str == '':
            break
        print(get_new_str(str))
