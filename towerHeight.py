# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 14:59:08 2020

@author: skadhikarla
"""

def tower(w, x, w_x, y, w_y, z, w_z):
    if(w < 0):
        return 0
    elif(w == 0):
        return 1
    else:
        return tower(w-w_x,x-1,w_x,y,w_y,z,w_z) + tower(w-w_y,x,w_x,y-1,w_y,z,w_z) + tower(w-w_z,x,w_x,y,w_y,z-1,w_z)
    
if __name__ == "__main__":
    G, B, R = 3, 2, 1
    
    h = int(input("Tower Height : "))
    w_g = h // G #// maximum G can be used
    w_b = h // B #// maximum B can be used
    w_r = h // R #// maximum R can be used
    
    numOfTowers = 0
    
    if(h > 0):
        numOfTowers = tower(h,w_g,G,w_b,B,w_r,R)
    
    print(numOfTowers)
    
    