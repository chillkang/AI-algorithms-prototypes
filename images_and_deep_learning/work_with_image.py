# -*- coding: utf-8 -*-

import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageChops


########## Section 2 −<Loading and Displaying Images>####################### 
# load image
img = cv2.imread('elephant.jpeg')

# display the image using Matplotlib and save image
plt.imshow(img)
plt.show()
cv2.imwrite('elephant_opencv.png', img)

# load image converted into a RGB space
im_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# display and save image
plt.imshow(im_rgb)
plt.show()
cv2.imwrite('elephant_matplotlib.png', im_rgb)

# load image in grayscale
img_gray = cv2.imread('elephant.jpeg', cv2.IMREAD_GRAYSCALE)

# display and save image
plt.imshow(img_gray)
plt.show()
cv2.imwrite('elephant_gray.png', img_gray)
##############################################################################

########## Section 3 −<Cropping>############################################## 
# print dimensions of image and crop out the small elephant. 
print(img.shape) 
cropped_img = im_rgb[400:900, 100:600]

# display and save image
plt.imshow(cropped_img)
plt.show()
cv2.imwrite('babyelephant.png', cropped_img)
##############################################################################

########## Section 4 -<Pixel-wise Arithmetic Operations>######################
# read in the image in color, and convert it to RGB space.
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img_rgb)
plt.show()
pixel= img_rgb[999, 1499]
print(pixel) # [168 171  94]

# add the value 256 to every single pixel in the image
img_rgb = img_rgb + 256

# check the image's datatype and the pixel values
print(img_rgb.dtype) #uint16
plt.imshow(img_rgb)
plt.show() 
pixel= img_rgb[999, 1499]
print(pixel) #[424 427 350]

# convert the image back to uint8 and display the image and the pixel values
img_rgb = img_rgb.astype(np.uint8)
print(img_rgb.dtype)  #unit8
plt.imshow(img_rgb)
plt.show()
pixel= img_rgb[999, 1499]
print(pixel) #[168 171 94]

# split the image into R,G,B channels seperately
bgr_img = cv2.imread("elephant.jpeg")
(b,g,r) = cv2.split(bgr_img)

plt.figure()
plt.imshow(b)
plt.show()
plt.figure()
plt.imshow(g)
plt.show()
plt.figure()
plt.imshow(r)
plt.show()

# add 256 to each one
b = cv2.add(b, 256)
g = cv2.add(g, 256)
r = cv2.add(r, 256)

plt.figure()
plt.imshow(b)
plt.show()
plt.figure()
plt.imshow(g)
plt.show()
plt.figure()
plt.imshow(r)
plt.show()
print(b.dtype) #uint8

#If you have a datatype that will not overflow if you add 100 to it (i.e. uint16) 
#then you can do simply use numpy.add() to do it:
#Most images are of type uint8 though so you'd want to clamp the output to a range of 0 to 255. 
#But when you do the add, you'd want to use a datatype that didn't overflow. 
#So there is some casting (astype()) needed:

# merge the channels back together and display the image
bgr_img = cv2.merge([b, g, r])

plt.figure()
plt.imshow(bgr_img)
plt.show()
cv2.imwrite('merged256.png', bgr_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

##############################################################################

########## Section 5 -<Resizing images>#######################################
# read the image in color and convert it to RGB space
img = cv2.imread('elephant.jpeg')
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# downsample the image by 10x in width and height and save the iamge
height, width = img_rgb.shape[:2]
downsample_img = cv2.resize(img_rgb, (round(width / 10), round(height / 10)), interpolation=cv2.INTER_AREA)
plt.imshow(downsample_img)
plt.show()
cv2.imwrite('elephant_10xdown.png', downsample_img)


upsized1 = cv2.resize(downsample_img, (round(width * 10), round(height * 10)), interpolation = cv2.INTER_NEAREST)
plt.imshow(upsized1)
plt.show()
upsized1_BGR = cv2.cvtColor(upsized1, cv2.COLOR_RGB2BGR)
cv2.imwrite('elephant_10xup_nearst_neighbor.png', upsized1_BGR)

upsized2 = cv2.resize(downsample_img, (round(width * 10), round(height * 10)), interpolation = cv2.INTER_CUBIC)
plt.imshow(upsized2)
plt.show()
upsized2_BGR = cv2.cvtColor(upsized2, cv2.COLOR_RGB2BGR)
cv2.imwrite('elephant_10xup_bicubic.png', upsized2_BGR)

img1 = Image.open('elephant.jpeg')
img2 = Image.open('elephant_10xup_nearst_neighbor.png')
diff1 = ImageChops.difference(img1, img2)
plt.imshow(diff1)
plt.show()
diff1 = np.array(diff1)
cv2.imwrite('elephant_diff_with_nearst_neighbor.png', diff1)

img3 = Image.open('elephant.jpeg')
img4 = Image.open('elephant_10xup_bicubic.png')
diff2 = ImageChops.difference(img3, img4)
plt.imshow(diff2)
plt.show()
diff2 = np.array(diff2)
cv2.imwrite('elephant_diff_with_bicubic.png', diff2)

sum1 = cv2.sumElems(diff1)
print(sum1) #(83336620.0, 71851852.0, 62169552.0, 0.0)
sum2 = cv2.sumElems(diff2)
print(sum2) #(83494819.0, 71880764.0, 62107822.0, 0.0)

cv2.waitKey(0)









