import math

def isPalindrome(x):
    s = str(x)
    l = len(s)
    if l == 1:
        return True
    i = 0
    j = l - 1
    while(i<=j and i<=math.floor(l/2)):
        if s[i] == s[j]:
            i += 1
            j -= 1
        else:
            return False
    return True


print(isPalindrome(121))