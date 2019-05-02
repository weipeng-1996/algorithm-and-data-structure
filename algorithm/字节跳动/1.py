import sys


def get_num(n):
    if n<3:
        return 1
    cattle_nums = [0 for i in range(11)]
    cattle_nums[1] = 0
    cattle_nums[2] = 1
    for j in range(2, n):
        if cattle_nums[10] != 0:
                cattle_nums[10] = 0
        for i in range(10, 1, -1):
            cattle_nums[i] = cattle_nums[i-1]
        cattle_nums[1] = 0
        for k in range(3, 8):
            cattle_nums[1] += cattle_nums[k]
    sum = 0
    for i in range(1, 11):
        sum += cattle_nums[i]
    return sum

if __name__ == '__main__':
    num = int(input())
    print(get_num(num))
        
