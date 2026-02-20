import cv2
import os

img_path = os.path.join(".", "image.jpg")
image = cv2.imread(img_path)


new_image = cv2.imwrite(os.path.join(".", "new_image.jpg"), image)
cv2.imshow('image', image)
cv2.imshow('new_image', new_image)

cv2.waitKey(0)