import math


def angle(ox, oy, fx, fy, px, py):
    dx1 = fx
    dy1 = fy
    dx2 = px - ox
    dy2 = py - oy
    angle1 = math.atan2(dy1, dx1)
    angle1 = int(angle1 * 180/math.pi)
    angle2 = math.atan2(dy2, dx2)
    angle2 = int(angle2 * 180/math.pi)
    if angle1 * angle2 >= 0:
        x = abs(angle1 - angle2)
    else:
        x = abs(angle1) + abs(angle2)
        if x > 180:
            x = 360 - 180
    return x


ox, oy, fx, fy, r, px, py = [int(i) for i in input().strip().split()]
x = angle(ox, oy, fx, fy, px, py)
print(x, r/2)
if x <= r/2:
    print(1)
else:
    print(0)
