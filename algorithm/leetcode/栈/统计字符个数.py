

def get_nums(s):
    arr_s = list(s)
    stack = []
    stack.append(arr_s[0])
    record = []
    for i in range(1, len(s)):
        if s[i] == stack[-1]:
            stack.append(s[i])
        else:
            record.append(stack[0])
            record.append(str(len(stack)))
            stack.clear()
            stack.append(s[i])
    record.append(stack[0])
    record.append(str(len(stack)))
    return ''.join(record)


if __name__ == '__main__':
    s = 'adddccccccqqqttq'
    print(get_nums(s))

    