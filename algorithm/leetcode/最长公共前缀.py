def longestCommonPrefix(strs):
    if strs == []:
        return ''
    for i in range(len(strs)):
        if not strs[i]:
            return ''
    s1 = strs[0]
    for i in range(1, len(strs)):
        j = 0
        l1 = len(strs[i])
        l2 = len(s1)
        while (j < l1 and j < l2 and s1[j] == strs[i][j]):
            j += 1
        else:
            if j == 0:
                return ''
            else:
                s1 = s1[:j]
    return s1

# 用ascll码


def longestCommonPrefix_ascll(strs):
    s1 = min(strs)
    s2 = max(strs)
    for i, s in enumerate(s2):
        if s != s1[i]:
            return s1[:i]
    return s1



if __name__ == '__main__':
    ss = ['aaa', 'aa', 'aaa']
    print(longestCommonPrefix(ss))


