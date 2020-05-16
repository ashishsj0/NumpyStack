#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 16 00:04:49 2020

@author: ashishsharma
"""

from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

im = Image.open('test_photo.jpg')

type(im)

arr = np.array(im)

arr.shape

plt.imshow(im)

type(arr)

gray = arr.mean(axis = 2)

plt.imshow(gray)

plt.imshow(gray, cmap='gray')
