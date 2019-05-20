def get_lcs_len(s1, s2):
    l1 = len(s1)
    l2 = len(s2)
    dp = [[0 for j in range(l2+1)] for i in range(l1+1)]
    for i in range(l1):
        for j in range(l2):
            if s1[i] == s2[j]:
                dp[i+1][j+1] = dp[i][j] + 1
            else:
                dp[i+1][j+1] = 0
    return dp


# 获得最长公共子串
def get_lcs(s1, s2, dp):
    temp = 0
    index_i = 0
    index_j = 0
    for i in range(1, len(dp)):
        for j in range(len(dp[0])):
            if dp[i][j] > temp:
                temp = dp[i][j]
                index_i = i
                index_j = j
    lcs = ['mm' for i in range(temp)]
    while(dp[index_i][index_j]!=0):
        lcs[temp-1] = s1[index_i-1]
        index_i -= 1
        index_j -= 1
        temp -= 1
    return ''.join(lcs)


    

if __name__ == '__main__':
    s1 = 'abcbassdwsabcba'
    s2 = 'werassfaswer'
    max_arr = get_lcs_len(s1,s1[-1::-1])
    print(get_lcs(s1,s2,max_arr))

