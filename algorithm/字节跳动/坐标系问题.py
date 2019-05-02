

def get_max_x_points(points, num):
    temp = points[0]
    for i in range(num):
        if points[i][0] > temp[0]:
            temp = points[i]
        if points[i][0] == temp[0] and points[i][1] > temp[1]:
            temp = points[i]
    return temp


def get_max_y_points(points, num):
    temp = points[0]
    for i in range(num):
        if points[i][1] > temp[1]:
            temp = points[i]
    return temp


def get_points(points, num):
    temp_points = points
    max_points = []
    temp1 = get_max_x_points(temp_points, len(temp_points))
    max_points.append(temp1)
    temp_points.remove(temp1)
    for i in range(num-1):
        temp1 = get_max_x_points(temp_points, len(temp_points))
        temp2 = get_max_y_points(max_points, len(max_points))
        if temp1[1] >= temp2[1]:
            max_points.append(temp1)
            temp_points.remove(temp1)
        else:
            temp_points.remove(temp1)
    return max_points


def min_points(points):
    num = len(points)
    temp = points[0]
    for i in range(num): 
        if temp[0] > points[i][0]:
            temp = points[i]
    return temp

        
if __name__ == '__main__':
    n = int(input())
    points_ins = [[0, 0] for i in range(n)]
    for i in range(n):
        temp = list(map(int, input().split()))
        points_ins[i] = temp
    max_points = get_points(points_ins, n)
    max_n = len(max_points)
    for i in range(max_n):
        temp = min_points(max_points)
        max_points.remove(temp)
        print(temp[0], temp[1])
