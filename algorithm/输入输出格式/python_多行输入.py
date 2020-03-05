import sys


if __name__ == '__main__':
    for i in range(5):
        line = sys.stdin.readline().strip()
        print(line, ' ', type(line))
        array = list(map(int, line.split()))
        print(array)
    # for line in sys.stdin:
    #     m, n = map(int, line.strip().split(' '))
    #     print(sum(m, n))
        
