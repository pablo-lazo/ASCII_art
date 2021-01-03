# -*- coding: utf-8 -*-.
"""
Created on Fri Jan  1 16:19:33 2021

@author: pablo
"""
from PIL import Image
from scripts.getAverageL import getAverageL

# Defining Grayscale levels
# Grayscale levels values from:
# http://paulbourke.net/dataformats/asciiart/

# 70 levels of gray
gscale1 = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~i!lI;:,^`. "

# 10 levels of gray
gscale2 = "@%#*+=-:. "


def convertImagetoAscii(fileName, cols, scale, moreLevels):
    """
    Given Image and dimensions (rows, cols), returns an m*n list of characters.

    Parameters
    ----------
    fileName : valid image file
    cols : int
        number of columns for ASCII image. Default is set to 80.
    scale: float
        aspect ratio for ASCII image. Default is set to 0.43 (Courier font).
    moreLevels: str
        custom grayscale provided by user.
    """
    # declare globals
    global gscale1, gscale2

    # open image and convert to grayscale
    image = Image.open(fileName).convert("L")

    # storing image dimensions
    W, H = image.size[0], image.size[1]

    print("input image dims: %d x %d" % (W, H))

    # compute tile width
    w = W/cols

    # compute tile height based on the aspect ratio and scale of the font
    h = w/scale

    # compute the number of rows to use in the final grid
    rows = int(H/h)

    print("cols: %d, rows: %d" % (cols, rows))
    print("tile dims: %d x %d" % (w, h))

    # check if image size is too small
    if cols > W or rows > H:
        print("Image too small for specified cols!")
        exit(0)

    # Generating ASCII Image

    AsciiImg = []

    # Generate list of tile dimensions
    for j in range(rows):
        y1 = int(j*h)
        y2 = int((j+1)*h)
        # correct last tile
        if j == rows - 1:
            y2 = H
        # append empty string
        AsciiImg.append("")
        for i in range(cols):
            # crop to image to fit the tile
            x1 = int(i*w)
            x2 = int((i+1)*w)
            # correct last tile
            if i == cols - 1:
                x2 = W

            # crop the image to extract the tile into another Image object
            img = image.crop((x1, y1, x2, y2))

            # get average luminance
            avg = int(getAverageL(img))

            # look up ASCII character matching average luminance (avg)
            if moreLevels:
                gsval = gscale1[int((avg*69)/255)]
            else:
                gsval = gscale2[int((avg*9)/255)]

            # append the ASCII character to the string
            AsciiImg[j] += gsval

    return AsciiImg
