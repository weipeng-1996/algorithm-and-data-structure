import sys

def count1(s):
    count = 0
    for i in range(len(s)):
        if(s[i] == '1'):
            count += 1
    return count


if __name__ == "__main__":
    n, k = [int(i) for i in input().strip().split()]
    s = input()
    b = [ 0 for i in range(n)]
    b[0] = s[0]
    for i in range(1, k):
        count = count1(b[:i])
        if s[i] == '1':
            count += 1
        if count % 2 == 0:
            b[i] = '0'
        else:
            b[i] = '1'
    temp = 1
    for i in range(k, n):
        count = count1(b[temp:n-k+temp])
        if s[i] == '1':
            count += 1
        if count % 2 == 0:
            b[i] = '0'
        else:
            b[i] = '1'
        temp += 1
    print(''.join(b))


    
