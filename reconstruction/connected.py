#for paths
import os
import sys
sys.path.append(r"C:\Users\jeanbaptiste\Desktop\chaipas")
#Librairy for treating pictures
import cv2
from PIL import Image

#Here numpy generate matrix
import numpy as np

#Show, Open, Create black picture
from starter.operation import open_picture
from starter.operation import show_picture
from starter.operation import blanck_picture
from starter.operation import find_first_points
from starter.operation import incrementation

from reconstruction.connected_function import treat_mini
from reconstruction.connected_function import end_condition
from reconstruction.connected_function import drawing
from reconstruction.connected_function import raising
from reconstruction.connected_function import schema_dico
from reconstruction.connected_function import add_list_next_last
from reconstruction.connected_function import road_test


def corner4(width, height, blanck, gray,
            oki_picture, x, y, dico_picture, nb):

    listex = [x+1,        x,        x+1,  x-1]
    listey = [y,          y+1,      y-1,  y+1]

    road_test(listex, listey, width, height, blanck, gray,
              oki_picture, "corner4", 1, 1, x, y, dico_picture, nb, 1, 0)


def lign_vertical(width, height, blanck, gray,
                  oki_picture, x, y, dico_picture, nb):

    for i in range(2):

        listex = [x,       x+1,     x+1]
        listey = [y+1,     y+1,      y-1]

        if i == 0:
            road_test(listex, listey, width, height, blanck, gray,
                      oki_picture, 'lign verticale1', 1, 0, x, y,
                      dico_picture, nb, 0, 0)
        elif i == 1:
            road_test(listex, listey, width, height, blanck, gray,
                      oki_picture, 'lign verticale2', -1, 0, x, y,
                      dico_picture, nb, 0, 0)


def corner7(width, height, blanck, gray,
              oki_picture, x, y, dico_picture, nb):

    listex = [x-1,   x,      x+1,   x-1]
    listey = [  y,   y+1,    y+1,   y-1]

    road_test(listex, listey, width, height, blanck, gray,
              oki_picture, "corner7", -1, 1, x, y, dico_picture, nb, 0, 1)


def lign_horizontal(width, height, blanck, gray,
                    oki_picture, x, y, dico_picture, nb):
    
    for i in range(2):
        listex = [x,       x+1,     x+1]
        listey = [y+1,     y+1,      y-1]
        if i == 0:
            road_test(listex, listey, width, height, blanck, gray,
                      oki_picture, 'lign horrizontale1', 0, -1, x, y,
                      dico_picture, nb, 0, 0)
        elif i == 1:
            road_test(listex, listey, width, height, blanck, gray,
                      oki_picture, 'lign horrizontale2', 0, 1, x, y,
                      dico_picture, nb, 0, 0)


def corner5(width, height, blanck, gray,
            oki_picture, x, y, dico_picture, nb):

    listex = [x+1,   x-1,      x,   x+1,  x-1]
    listey = [y,       y,     y-1,  y-1,  y+1]

    road_test(listex, listey, width, height, blanck, gray,
              oki_picture, "corner5", -1, -1, x, y, dico_picture, nb, 0, 1)


def corner6(width, height, blanck, gray,
            oki_picture, x, y, dico_picture, nb):

    listex = [x-1,    x,      x+1,   x-1]
    listey = [y,     y-1,    y+1,   y-1] 

    road_test(listex, listey, width, height, blanck, gray,
              oki_picture, "corner6", 1, -1, x, y, dico_picture, nb, 0, 1)




def main_connected(original, picture, minini):
    schema = ['corner4', 'lign verticale', 'corner7', 'lign horrizontale', 'corner5', 'corner6']

    img = open_picture(original)
    copy = img.copy()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blanck = blanck_picture(img)

    #Sort list last, next picture 
    oki_picture = add_list_next_last(picture)
    #print(oki_picture)


    #Treat minini doublon list of list to list of list.
    treat_minini = treat_mini(minini)
    #print(minini)
    #print(treat_minini)

    #Schema with passation.
    dico_picture = schema_dico(len(treat_minini))
    #print(dico_picture)


    for nb in range(len(treat_minini)):
        blanck = blanck_picture(img)

        img1 = open_picture(oki_picture[nb][0])
        img2 = open_picture(oki_picture[nb][1])

        gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
        gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

        #Recuperate dimensions of picture
        height, width, chann = img1.shape

        #position of current form
        x = treat_minini[nb][0]
        y = treat_minini[nb][1]

        #Next form in red
        drawing(blanck, gray2, (0, 0, 255))



        find = False
        for i in schema:

            x = treat_minini[nb][0]
            y = treat_minini[nb][1]

            if i == "corner4":
                corner4(width, height, blanck, gray,
                         oki_picture, x, y, dico_picture, nb)

            elif i == 'lign verticale':
                lign_vertical(width, height, blanck, gray,
                              oki_picture, x, y, dico_picture, nb)

            elif i == 'corner7':
                corner7(width, height, blanck, gray,
                        oki_picture, x, y, dico_picture, nb)

            elif i == 'lign horrizontale':
                lign_horizontal(width, height, blanck, gray,
                                oki_picture, x, y, dico_picture, nb)

            elif i == 'corner5':
                corner5(width, height, blanck, gray,
                        oki_picture, x, y, dico_picture, nb)

            elif i == 'corner6':
                corner6(width, height, blanck, gray,
                        oki_picture, x, y, dico_picture, nb)


    print(dico_picture)
    print("")
    print(treat_minini)
    print("")
    print(oki_picture)


    return dico_picture, treat_minini, oki_picture



minini = [[[65, 33], [71, 35]], [[109, 60], [103, 56]], [[109, 83], [109, 89]],
          [[94, 140], [88, 134]], [[107, 165], [117, 165]]]


picture = ['../images/blanck/6blanck.jpg', '../images/blanck/2blanck.jpg', '../images/blanck/4blanck.jpg',
           '../images/blanck/8blanck.jpg', '../images/blanck/10blanck.jpg', '../images/blanck/0blanck.jpg',]




#main_connected("ici.png", picture, minini)
