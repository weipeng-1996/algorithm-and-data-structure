'''链接：https://www.nowcoder.com/questionTerminal/e6e57ef2771541dfa2f1720e50bebc9a'''


def get_max_value(arr):
    stack = []
    arr.append(0)
    i = 0
    result = 0
    presum = []
    sum = 0
    while(i<len(arr)):
        if not stack or arr[i] >= stack[-1]:
            presum.append(sum)
            sum = 0
            stack.append(arr[i])
            i += 1
        else:
            min = stack.pop()
            sum += (min+presum.pop())
            result = max(result, min*sum)
    return result

if __name__ == '__main__':
    num = int(input())
    array = list(map(int, input().split()))
    print(get_max_value(array))



