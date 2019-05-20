
def get_min_num(coin, m):
    n = len(coin)
    coin.sort()
    min_num = [9999 for i in range(m+1)]
    min_num[0] = 0
    for i in range(1, m+1):
        for j in range(n):
            if i >= coin[j]:
                min_num[i] = min(min_num[i-coin[j]]+1, min_num[i])
            else:
                break
    return min_num

if __name__ == '__main__':
    coin_ins = [3, 6, 7]
    money = 22
    print(get_min_num(coin_ins, money))
            
