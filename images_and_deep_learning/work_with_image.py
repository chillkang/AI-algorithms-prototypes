# -*- coding: utf-8 -*-

import cv2
import numpy as np
import matplotlib.pyplot as plt

########## Section 2.a −<Loading and Displaying Images>####################### 
# load image
img = cv2.imread('elephant.jpeg')

# display image
plt.imshow(img)
plt.show()
cv2.imwrite('elephant_opencv.png', img)
##############################################################################
