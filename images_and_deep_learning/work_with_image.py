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

########## Section 2.b −<Loading and Displaying Images>####################### 
# load image
im_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# display image
plt.imshow(im_rgb)
plt.show()
cv2.imwrite('elephant_matplotlib.png', im_rgb)
##############################################################################