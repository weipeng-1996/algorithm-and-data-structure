# 给定一个字符串s，你可以从中删除一些字符，使得剩下的串是一个回文串。
# 如何删除才能使得回文串最长呢？
# 输出需要删除的字符个数。
# 输入数据有多组，每组包含一个字符串s，且保证:1<=s.length<=1000.
import sys

def get_lcs(str1, str2):
    l1 = len(str1)
    l2 = len(str2)
    max_lcs = [[0 for j in range(l2+1)] for i in range(l1+1)]
    for i in range(1, l1+1):
        for j in range(1, l2+1):
            if str1[i-1] == str2[j-1]:
                max_lcs[i][j] = max_lcs[i-1][j-1] + 1
            else:
                max_lcs[i][j] = max(max_lcs[i-1][j], max_lcs[i][j-1])
    return max_lcs

def get_del_num(str):
    l = len(str)
    str_reverse = str[-1::-1]
    max_str_lcs = get_lcs(str, str_reverse)
    num =  l - max_str_lcs[l][l]
    return num


if __name__ == '__main__':
    while True:
        line = sys.stdin.readline().strip()
        if line == '':
            break
        print(get_del_num(line))
