

def get_lcs(str1, str2):
    l1 = len(str1)
    l2 = len(str2)
    # max_lcs[i][j] = str1[:i] 与 str2[:j]的lcs的长度
    max_lcs = [[0 for i in range(l2+1)] for j in range(l1+1)]
    for i in range(1, l1+1):
        for j in range(1, l2+1):
            if str1[i-1] == str2[j-1]:
                max_lcs[i][j] = max_lcs[i-1][j-1] + 1
            else:
                max_lcs[i][j] = max(max_lcs[i-1][j], max_lcs[i][j-1])
    return max_lcs


def lcs(str1, str2, max_lcs):
    l1 = len(str1)
    l2 = len(str2)
    lcs = ['mm' for i in range(max_lcs[l1][l2])]
    l3 = max_lcs[l1][l2]-1
    while(l1 > 0 and l2 > 0):
        if str1[l1-1] == str2[l2-1]:
            lcs[l3] = str1[l1-1]
            l1 -= 1
            l2 -= 1
            l3 -= 1
        elif max_lcs[l1-1][l2] <= max_lcs[l1][l2-1]:
            l2 -= 1
        else:
            l1 -= 1
    return lcs





if __name__ == '__main__':
    str1 = '13456778'
    str2 = '357486782'
    lcs_matrix = get_lcs(str1, str2)
    print(lcs_matrix)
    res = lcs(str1, str2, lcs_matrix)
    print(res)
