import sys
sys.path.append('..')
import CheckPointInPolygonCplusplus as PIPolygon
import cv2
import numpy as np
from random import randrange
print()

if __name__ == '__main__':
    img = np.zeros((300, 300, 3), dtype=np.float32)

    polygon = [[1, 4], [100, 12], [200, 200]]
    img = cv2.polylines(img, [np.array(polygon, dtype=np.int32)], isClosed = True, thickness = 2, color = (0, 255, 0))

    blue = (255, 0, 0)
    red = (0, 0, 255)

    # Check a single point whether is in the polygon or not
    x = randrange(300)
    y = randrange(300)
    check = PIPolygon.PointInPolygon((x, y), polygon)
    if check:
        img = cv2.circle(img, (x, y), radius = 10, thickness=-1, color = blue)
    else:
        img = cv2.circle(img, (x, y), radius = 10, thickness=-1, color = red)


    # Check a list of points whether is in the polygon or not
    points = [(131, 192), (129, 23), (149, 129), (112, 182), (192, 295), (73, 49), (220, 135), (140, 180), (99, 159), (132, 14)]
    check = PIPolygon.PointsInPolygon(points, polygon)
    for i in range(len(check)):
        if check[i] == True:
            img = cv2.circle(img, points[i], radius = 5, thickness=-1, color = blue)
        else:
            img = cv2.circle(img, points[i], radius = 1, thickness=-1, color = red)
    cv2.imwrite('test.jpg', img)
