import sys
import itertools

def get_num(loc, n, d):
    loc.sort()
    number = 0
    left = 0
    right = 0
    for i in range(n):
        for j in range(i+1, n):
            if loc[j] - loc[i] >= d:
                temp = j - i + 1
                if temp > number:
                    number = temp
                    left = i
                    right = j
                break
    solu = len(list(itertools.combinations(loc[left:right+1], 3)))
    return solu
            

    


if __name__ == '__main__':
    n, d = tuple(map(int, input().split()))
    location = list(map(int, input().split()))
    num = get_num(location, n, d)
    print(num)
