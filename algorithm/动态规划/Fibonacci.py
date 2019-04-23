
# Fibonacci (n) = 1;   n = 0

# Fibonacci(n) = 1 ;   n = 1

# Fibonacci(n) = Fibonacci(n-1) + Fibonacci(n-2)

#递归版本

def fib1(n):
    if n <= 1:
        return n
    return fib1(n-1)+fib1(n-2)

# 动态规划-自顶向下(备忘录法)

def fib2(n):
    if n <= 1:
        return n
    arr = [-1 for i in range(n+1)]
    return fib_temp(n, arr)

def fib_temp(n, arr):
    if arr[n] != -1:
        return arr[n]
    if n <= 2:
        arr[n] = 1
    else:
        arr[n] = fib_temp(n-1, arr) + fib_temp(n-2, arr)
    return arr[n]

# 动态规划-自底向上

def fib3(n):
    if n <= 1:
        return n
    arr = [0 for i in range(n+1)]
    arr[1] = 1
    for i in range(2, n+1):
        arr[i] = arr[i-1] + arr[i-2]
    return arr[n]

# 自底向上优化

def fib4(n):
    if n <= 1:
        return n
    temp0 = 0
    temp1 = 1
    for i in range(2, n+1):
        temp = temp0 + temp1
        temp0, temp1 = temp1, temp
    return temp


if __name__ == '__main__':
    print(fib2(9))
    print(fib4(9))
    print(fib4(6))
