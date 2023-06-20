import math


def iScollision(x1, x2, y1, y2):
    x = math.pow((x2 - x1), 2)
    y = math.pow((y2 - y1), 2)

    dist = math.sqrt(x + y)
    # print(dist)
    if dist <= 115:
        return True

    else:
        return False
