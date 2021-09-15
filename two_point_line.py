point1 = (0,2)
point2 = (1,4)
x = 2

def y_coordinate(point1, point2, x):
    m = (point1[1]-point2[1])/(point1[0]-point2[0])
    print(m)
    b = point1[1] - m * point1[0]
    print(m)
    y = m * x + b
    return y


if __name__ == "__main__":
    print(y_coordinate(point1, point2, x))
