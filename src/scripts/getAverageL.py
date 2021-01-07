# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 20:24:42 2020

@author: pablo
"""
import numpy as np


def getAverageL(image):
    """
    Given grayscaled PIL Image, return average value of grayscale value.

    Returns
    -------
        int: Average luminosity of image.
    """
    im = np.array(image)
    if len(im.shape) == 2:
        w, h = im.shape
        return np.average(im.reshape(w * h))
    else:
        return None
