
def get_min(matrix, n, m):
    if n == 1 and m == 1:
        return 0
    dp = = [[0 for i in range(m)] for j in range(n)]
    for i in range(n):
        for j in range(m-1):
            if matrix[i][j] == matrix[i][j+1]:
                dp[i][j+1] += 1
            elif i > 0:
                if matrix[i][j] == matrix[i-1][j]:
                    dp[i][j+1] += 1





if __name__ == '__main__':
    n, m = tuple(map(int, input().split()))
    matrix_ins = [[0 for i in range(m)] for j in range(n)]
    for i in range(n):
        temp = list(map(int, input().split()))
        for j in range(m):
            matrix_ins[i][j] = temp[j]
    print(4)
