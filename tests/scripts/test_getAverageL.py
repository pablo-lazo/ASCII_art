# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 16:51:52 2021

@author: pablo
"""

import pytest
from ASCII_art.src.scripts.getAverageL import getAverageL


def test_for_L_converted_image():
    assert getAverageL([[10, 20, 30], [40, 50, 60], [70, 80, 90]]) == 50.0


def test_for_RGB_image():
    assert getAverageL([[[255, 0, 0], [0, 255, 0], [0, 0, 255]],
                        [[0, 0, 255], [255, 0, 0], [0, 255, 0]],
                        [[0, 255, 0], [0, 0, 255], [255, 0, 0]]]) is None
