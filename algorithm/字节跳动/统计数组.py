#coding=utf-8
import sys


def get_str(s):
    index = 1
    arr = []
    l = len(s)
    i = 1
    while i < l:
        if i == l-1 and s[i] == s[i-1]:
            arr.append(s[i])
            arr.append(str(i-index+1))
            break
        elif i == l-1 and s[i] != s[i-1]:
            arr.append(s[index])
            arr.append(str(i-index))
            arr.append(s[l-1])
            arr.append('1')
            break
        if s[i] == s[i-1]:
            i += 1
            continue
        elif i == 1:
            arr.append(s[0])
            arr.append('1')
            i += 1
        else:
            arr.append(s[index])
            arr.append(str(i-index))
            index = i
            i += 1
    s1 = ''.join(arr)
    if len(s1) > l:
        return s
    else:
        return s1


if __name__ == '__main__':
    s = 'abbbccccccdddda'
    print(get_str(s))
