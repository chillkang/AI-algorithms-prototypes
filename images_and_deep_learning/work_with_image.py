# -*- coding: utf-8 -*-

import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


########## Section 2.a −<Loading and Displaying Images>####################### 
# load image
img = cv2.imread('elephant.jpeg')

# display and save image
plt.imshow(img)
plt.show()
cv2.imwrite('elephant_opencv.png', img)

# load image
im_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# display and save image
plt.imshow(im_rgb)
plt.show()
cv2.imwrite('elephant_matplotlib.png', im_rgb)

im_pillow = np.array(Image.open('elephant.jpeg'))
im_bgr = cv2.cvtColor(im_pillow, cv2.COLOR_RGB2BGR)
cv2.imwrite('elephant_matplotlib.png', im_bgr)

# load image
img_gray = cv2.imread('elephant.jpeg', cv2.IMREAD_GRAYSCALE)

# display and save image
plt.imshow(img_gray)
plt.show()
cv2.imwrite('elephant_gray.png', img_gray)
##############################################################################

########## Section 3 −<Cropping>############################################## 
# print dimensions and load image
print(img.shape) 
cropped_img = im_rgb[400:900, 100:600]

# display and save image
plt.imshow(cropped_img)
plt.show()
cv2.imwrite('babyelephant.png', cropped_img)
##############################################################################

########## Section 4.a -<Pixel-wise Arithmetic Operations>####################
# Read in the image in color, and convert it to RGB space.

img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img_rgb)

img_rgb = img_rgb + 256

print(img_rgb.dtype) #uint16
pixel= img_rgb[999, 1499]
print(pixel) #[424 427 350]

img_rgb = img_rgb.astype(np.uint8)
print(img_rgb.dtype)  #unit8
pixel= img_rgb[999, 1499]
print(pixel) #[168 171 94]

#The RGB/BGR values are [0, 255] BECAUSE uint8 has that range. 
#The reason why Uint8 is very common is because it is the standard way to display images, 
#in which each pixel ranges between 0 and 255.


bgr_img = cv2.imread("elephant.jpeg")
(b,g,r) = cv2.split(bgr_img)
cv2.imshow("Red", r)
cv2.imshow("Green", g)
cv2.imshow("Blue", b)
cv2.waitKey(0)

#x = np.uint8([256])
b = cv2.add(b, 256)
g = cv2.add(g, 256)
r = cv2.add(r, 256)
cv2.imshow("Blue256", b)
cv2.imshow("Green256", g)
cv2.imshow("Red256", r)
cv2.waitKey(0)


bgr_img = cv2.merge([b, g, r])
cv2.imshow("Merged", bgr_img)
cv2.waitKey(0)
cv2.imwrite('merged.png', bgr_img)

##############################################################################




