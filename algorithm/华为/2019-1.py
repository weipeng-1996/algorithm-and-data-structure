
def get_num(l):
    count = 0
    for i in range(1, int(l/3)):
        j = l - l * l / (2 * l - 2 * i)
        if i < j and j - int(j) < 1e-5:
            count += 1
    return count


if __name__ == '__main__':
    p = int(input())
    print(get_num(p))