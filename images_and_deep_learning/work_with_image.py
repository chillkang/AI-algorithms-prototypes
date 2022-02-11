# -*- coding: utf-8 -*-

import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


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

im_pillow = np.array(Image.open('elephant.jpeg'))
im_bgr = cv2.cvtColor(im_pillow, cv2.COLOR_RGB2BGR)
cv2.imwrite('elephant_matplotlib.png', im_bgr)
##############################################################################

########## Section 2.c −<Loading and Displaying Images>####################### 
# load image
img_gray = cv2.imread('elephant.jpeg', cv2.IMREAD_GRAYSCALE)

# display image
plt.imshow(img_gray)
plt.show()
##############################################################################

