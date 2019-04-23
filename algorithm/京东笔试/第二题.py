
if __name__ == '__main__':
    n, e = tuple(map(int, input().split()))
    edge_list = [[0 for i in range(n)] for j in range(n)]
    for i in range(e):
        a, b = tuple(map(int, input().split()))
        edge_list[a-1][b-1] = 1
    p = [0 for i in range(n)]
    for i in range(n):
        for j in range(n):
            if edge_list[i][j] == 1:
                p[j] += 1
    for i in range(n):
        
    print(p)
