import sys


if __name__ == "__main__":
    n = int(input())
    time = []
    for i in range(n):
        hi, mi = [int(j) for j in input().strip().split()]
        time.append(hi*60+mi)
    x = int(input())
    hi, mi = [int(j) for j in input().strip().split()]
    start_time = hi*60+mi
    judge = start_time - x
    time.sort()
    count = -1
    for i in range(n):
        if(time[i]>judge):
            count = i - 1
            break
    h = int(time[count] / 60)
    m = int(time[count] % 60)
    print(h, m)

    
