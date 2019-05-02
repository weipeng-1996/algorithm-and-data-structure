import sys
from collections import Counter

def get_nums(numbers):
    n = len(numbers)
    return Counter(numbers)


if __name__ == '__main__':
    ll = list(map(int, input().split()))
    ss = Counter(ll)
    print(ss.most_common()[-1][0])