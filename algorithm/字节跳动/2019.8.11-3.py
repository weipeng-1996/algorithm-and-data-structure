import sys


if __name__ == "__main__":
    n = int(input())
    b = [int(i) for i in input().strip().split()]
    min_index = b.index(min(b))
    maxl = 100
    maxr = 100
    total = 100
    i = min_index-1
    j = min_index+1
    while (i >= 0) or (j <= len(b) - 1):
        if i > 0:
            if(b[i]>b[i+1]):
                maxl += 100
                total += maxl
            elif b[i] < b[i+1]:
                maxl -= 100
                total += maxl
            else:
                total += maxl
        i -= 1
        if j < len(b) -1:
            if b[j] > b[j-1]:
                maxr += 100
                total += maxr
            elif b[j] < b[j-1]:
                maxr -= 100
                total += maxr
            else:
                total += maxr
        j += 1
    print(total)

  


    
