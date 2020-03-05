# 使用栈结构
def isValid(s):
    l = len(s)
    stack = []
    kkh = ['(', '{', '[']
    bkh = [')', '}', ']']
    for i in range(l):
        # 遇到左开括号 压栈
        if s[i] in kkh:
            stack.append(s[i])
        # 遇到非左开括号，且栈为空false
        elif not stack:
            return False
        # 判断是否匹配
        else:
            if s[i] == bkh[kkh.index(stack.pop())]:
                continue
            else:
                return False
    if not stack:
        return True
    else:
        return False

# 技巧


class Solution:
    def isValid(self, s):
        while '{}' in s or '()' in s or '[]' in s:
            s = s.replace('{}', '')
            s = s.replace('[]', '')
            s = s.replace('()', '')
        return s == ''

s1 = input()
print(isValid(s1))
