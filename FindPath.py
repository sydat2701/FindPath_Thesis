import re
from FindPath_Multiroad.FillGrid import *
import FindPath_Multiroad.FillGrid
from FindPath_Multiroad.FindPathCplusplus import BFS 
import cv2 
import math
import time

def findPath(CARS, ROAD, SLOTS, SELECTED_SLOTS, H, W, N, M, image=None, returnImages=True):
    start_time = time.time() 
    grid = fill_grid(CARS, ROAD, SLOTS, H, W, N, M)
    end_time = time.time()
    #print(f'Fill Grid time ={end_time - start_time} second')

    start_time = time.time() 
    slotsCell = convert_slotsPoint_slotsCell(SLOTS, H, W, N, M)
    selected_slotsCell = convert_slotsPoint_slotsCell(SELECTED_SLOTS, H, W, N, M)
    findPath = BFS(N, M, grid, slotsCell, selected_slotsCell)
    end_time = time.time()
    #print(f'Find Path time ={end_time - start_time} second')

    start_time = time.time() 
    pathsCell = findPath.shortestPath()
    pathsPoint = []
    for path in pathsCell:
        pathPoint = []
        for point in path:
            x = point//M;
            y = point%M;
            pathPoint.append(convert_cell_to_point(x, y, H, W, N, M))
        pathsPoint.append(pathPoint)
    
    images = []
    tmp_img = draw(image, grid, H, W, N, M)
    img_default=tmp_img.copy()
    if returnImages:
        if image is None:
            raise ValueError("Image is required. Missing value of image")
        else:
            for i in range(len(CARS)):
                car = CARS[i]
                path = pathsPoint[i]
                img = tmp_img.copy()
                for point in path:
                    h, w = point
                    img = cv2.circle(img, (int(w), int(h)), radius=2, color=(0,0,255), thickness=-1)
                    img_default=cv2.circle(img_default, (int(w), int(h)), radius=2, color=(0,0,255), thickness=-1)
                    
                images.append(img)                
    end_time = time.time()
    #print(f'Modify output time ={end_time - start_time} second')
    
    if returnImages:
        return images, img_default
    return pathsPoint, None       
# Result = pathsPoint or images

def draw_path(paths, CARS, ROAD, SLOTS, H, W, N, M, img):
    grid = fill_grid(CARS, ROAD, SLOTS, H, W, N, M)
    image = img.copy()
    image = draw(image, grid, H, W, N, M)
    i = 0
    for path in paths:
        for point in path:
            h, w = point
            image = cv2.circle(image, (int(w), int(h)), radius=2, color=(0,0,255), thickness=-1)
    #cv2.imwrite('test.jpg', image)
    return image

