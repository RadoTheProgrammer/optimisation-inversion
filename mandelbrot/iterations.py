import math
import pygame
import numpy as np
import pandas as pd

from PIL import Image
from tqdm import tqdm
def iterations(c:complex,n:int = 100):
    for i in range(n):
        if i:
            try:
                val = last_val**2 + c
            except OverflowError:
                return i
        else:
            val = complex()
        if math.isnan(val.real):
            #return False
            return i
        last_val = val
    return 0
def Rect(top=0,bottom=0,width=0,height=0,**kwargs):
    rect = pygame.Rect(top,0,width,height)
    rect.bottom = bottom
    for key,value in kwargs.items():
        setattr(rect,key,value)
    return rect

def mandelbrot(rect:pygame.Rect,precision=0.01): # warning: flipped and reversed coords
    widthp = int(rect.width/precision)
    heightp = int(rect.height/precision)

    arr = np.zeros((heightp,widthp))
    arr_mandelbrot = np.zeros((heightp,widthp))
    arr_color = np.zeros((heightp,widthp,3),dtype=np.uint8)
    print(arr.shape)
    for y in tqdm(range(heightp)):
        imag = rect.top+y*precision
        for x in range(widthp):
            real = rect.left+x*precision
            c = complex(real,imag)
            #print(c)
            i = iterations(c)
            if i:
                is_mandelbrot = 0
                color = (255,255,255)
            else:
                is_mandelbrot = 1
                color = (0,0,0)
            arr[y,x] = i
            arr_mandelbrot[y,x] = is_mandelbrot
            arr_color[y,x] = color
    values, counts = np.unique(arr, return_counts=True)
    value_count = pd.Series(counts,values)
    #print(value_count)
    return arr_color
r = Rect(center=(0,0),width=1,height=1)
print(r)
arr_color = mandelbrot(r)
heightp,widthp,_ = arr_color.shape
print(arr_color.shape)
Image.fromarray(arr_color).save("result.png")





