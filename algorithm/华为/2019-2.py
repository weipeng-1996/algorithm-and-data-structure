import sys

if __name__ == '__main__':
    matrix = [[1, 2, 3, 4, 5], [11, 12, 13, 14, 15], [21, 22, 23, 24, 25],
              [31, 32, 33, 34, 35], [41, 42, 43, 44, 45]]
    while 1:
        hl = [0 for i in range(6)]
        judge = [0 for i in range(6)]
        cat = []
        line = sys.stdin.readline().strip()
        # 把每一行的数字分隔后转化成int列表
        if line == '':
            break
        arr = list(map(int, line.split()))
        for i in range(6):
            for j in range(5):
                if arr[i] in matrix[j]:
                    hl[i] = (j+1) * 5 - (4 - matrix[j].index(arr[i]))
        hl.sort()
        cat.append(hl[0])
        for i in range(1, 6):
            if (hl[i] - 1) in cat or (hl[i]+1) in cat or (hl[i]-5) in cat or (hl[i]+5) in cat:
                cat.append(hl[i])
        if len(cat) == 6:
            print(1)
        else:
            print(0)
        
    
