import sys


if __name__ == '__main__':
    n, v = tuple(map(int, input().split()))
    prop = list(map(int, input().split()))
    m = list(map(int, input().split()))
    x_list = [0 for i in range(n+1)]
    sum = 0
    index = 0
    for i in range(n):
        sum += prop[i]
        x_list[i] = m[i]/prop[i]
    x_list[n] = v/sum
    temp = x_list[0]
    for i in range(1, n+1):
        if temp > x_list[i]:
            temp = x_list[i]
            index = i
    max = round(sum*x_list[index], 4)
    print('%.4f' % max)
