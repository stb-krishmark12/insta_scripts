# Follow for more @stb_krishmark12

import cv2

img = cv2.imread("sample.jpeg.jpeg")#enter image name

gray_image = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
inverted_image = 255 - gray_image
blurred = cv2.GaussianBlur(inverted_image, (21, 21), 5)
inverted_blurred = 255 - blurred
pencil_sketch = cv2.divide(gray_image, inverted_blurred, scale=256.0)

cv2.imshow("Original image", img)
cv2.imshow("Pencil Sketched image", pencil_sketch)
cv2.waitKey(0)
