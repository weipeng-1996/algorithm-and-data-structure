import sys


if __name__ == "__main__":
    # 一行多变量输入
    # n = map(int, inpu`t().split())
    while True:
        m = sys.stdin.readline().strip()
        if m == '':
            break
        print(list(map(int, m.split())))
    [n_pm, n_chengxuyuan, n_idea] = [int(i) for i in input().strip().split()]
    
    '''
    money = []
    for i in range(m):
        # 读取每一行
        line = sys.stdin.readline().strip()
        # 把每一行的数字分隔后转化成int列表
        values = list(map(int, line.split()))
        for v in values:
            money.append(v)


    print(money)
'''
