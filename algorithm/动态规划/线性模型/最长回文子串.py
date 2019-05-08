

def longestPalindrome(s):
    l = len(s)
    dp = [[0 for j in range(l)] for i in range(l)]
    sub_str = ''
    len_sub = 0
    for i in range(l):
        for j in range(i+1):
            if i - j <= 1:
                if s[j] == s[i]:
                    dp[j][i] = 1
                    if (i-j+1) > len_sub:
                        sub_str = s[j:i+1]
                        len_sub = i - j + 1
            else:
                if s[j] == s[i] and dp[j+1][i-1]:
                    dp[j][i] = 1
                    if (i-j+1) > len_sub:
                        sub_str = s[j:i+1]
                        len_sub = i - j + 1
    return sub_str


if __name__ == '__main__':
    str = 'cbbd'
    print(longestPalindrome(str))
