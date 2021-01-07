# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 08:56:24 2020

@author: pablo lazo
"""
# %%

import argparse
from scripts.convertImagetoAscii import convertImagetoAscii

# main function


def main():
    """Given image and params converts to ASCII image.

    Params
    ------
        file: image file to convert to ASCII
        scale: aspect ratio of the ASCII image. Default 0.43.
        out: text file containing ASCII. Default out.txt.
        cols: number of columns of ASCII image. Default 80.
        morelevels: custom characters scale.
    """
    # Create parser and Command line options
    descStr = "This program converts an image into ASCII Art."
    parser = argparse.ArgumentParser(description=descStr)

    # add expected arguments
    parser.add_argument("--file", dest="imgFile", required=True)
    parser.add_argument("--scale", dest="scale", required=False)
    parser.add_argument("--out", dest="outFile", required=False)
    parser.add_argument("--cols", dest="cols", required=False)
    parser.add_argument("--morelevels", dest="moreLevels",
                        action="store_true")
    parser.add_argument("--invert", dest="invert", action="store_true")

    # parse arguments
    args = parser.parse_args()

    imgFile = args.imgFile
    outFile = "out.txt"
    if args.outFile:
        outFile = args.outFile

    # set scale default as 0.43, which suits a Courier font
    scale = 0.43
    if args.scale:
        scale = float(args.scale)

    # set cols
    cols = 80
    if args.cols:
        cols = int(args.cols)

    print("generating ASCII art")

    AsciiImg = convertImagetoAscii(imgFile, cols, scale, args.moreLevels,
                                   args.invert)

    # Writing the ASCII Art string to a file
    f = open(outFile, "w")

    # write each string in the list to the file
    for row in AsciiImg:
        f.write(row + "\n")

    # cleaning up
    f.close()
    print("ASCII art written to %s" % outFile)

# call main


if __name__ == "__main__":
    main()
