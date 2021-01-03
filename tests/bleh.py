# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 17:09:20 2021

@author: pablo
"""
import numpy as np
from PIL import Image

#%%
RGB = Image.open("data/RGB.jpg")

rgb = np.array(RGB)

print(rgb)
print(rgb.shape)

#%%

RGBW = Image.open("data/RGBW.jpg")

rgbw = np.array(RGBW)

print(rgbw)
print(rgbw.shape)

#%%

RGBW = Image.open("data/RGBW.jpg").convert("L")

rgbw = np.array(RGBW)

print(rgbw)
print(rgbw.shape)

#%%

RGB = Image.open("data/RGB.jpg").convert("L")

print(type(RGB))

rgb = np.array(RGB)

w, h = rgb.shape


print(type(rgb))
print(rgb)
print(rgb.shape)

avg = np.average(rgb.reshape(w*h))
print(avg)

#%%

a = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])

print(np.average(a))