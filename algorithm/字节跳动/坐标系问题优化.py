import sys


if __name__ == '__main__':
    n = int(sys.stdin.readline().strip())
    points_ins = [[0, 0] for i in range(n)]
    for i in range(n):
        temp = list(map(int, sys.stdin.readline().strip().split()))
        points_ins[i] = temp
    points_ins.sort(key=lambda x:x[1], reverse=True)
    max_points = []
    max_points.append(points_ins[0])
    for i in range(1, n):
        if points_ins[i][0] > max_points[-1][0]:
            max_points.append(points_ins[i])
        else:
            continue
    # max_points.sort(key=lambda x:x[0])
    for i in range(len(max_points)):
        print(max_points[i][0], max_points[i][1])
        


    
