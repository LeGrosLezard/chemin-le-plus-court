import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

from operation import open_picture
from operation import show_picture
from operation import blanck_picture



#Variables
R = cv2.RETR_TREE
P = cv2.CHAIN_APPROX_NONE

#Image
img = open_picture('images/lign_v1.jpg')
#New Images
copy = img.copy()
blanck = blanck_picture(img)


def recup_contours(img):

    edges = cv2.Canny(img, 255,200)
    contours, _ = cv2.findContours(edges, R, P)

    for cnts in contours:
        cv2.drawContours(blanck, [cnts], -1, (255,255,255), 1)
        #cv2.fillPoly(blanck, pts =[cnts], color=(255, 255, 255))
        (x, y, w, h) = cv2.boundingRect(cnts)

    return blanck





#Filter
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blanck = recup_contours(img)
blanck = cv2.cvtColor(blanck, cv2.COLOR_BGR2GRAY)



#PREMIERE DETECTION DU PREMIER POINTS NOIR
pts1 = 0; pts2 = 0;
pointsx = []; pointsy = [];

for y in range(blanck.shape[1]):
    for x in range(blanck.shape[0]):

        if blanck[x ,y] == 255:
            pointsx.append([x, y])
            pointsy.append(y)
        
x = pointsx[0][0]
y = pointsx[0][1]


copy[x, y]= 0, 0, 255



while True:
    listex = [x + 1, x]
    listey = [y,     y+1]

    for i in range(len(listex)):
        #print(blanck[listex[i], listey[i]])
        if blanck[listex[i], listey[i]] == 255:
            if i == 0:
                copy[x, y] = 0, 255, 0
                x += 1
            elif i == 1:
                copy[x, y] = 0, 0, 255
                y += 1
    


    copy1 = copy.copy()
    copy1 = cv2.resize(copy1, (800, 800))
    show_picture("copy1", copy1, 0, "")

































