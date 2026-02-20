import os
import cv2

image_path = os.path.join(".", "image.jpg")
image  = cv2.imread(image_path)
details = list(image.shape)

cropped_image = image[123:200, 123:200]
resized_image = cv2.resize(image, (round(details[0]/2), round(details[1]/2)))
cv2.imshow('resized_image', resized_image)
cv2.waitKey(0)

"""
import os
import cv2

video_path = os.path.join('.', "cutout.mp4")
video = cv2.VideoCapture(video_path)

rel = True
counter = 1
while rel:
    rel, frame = video.read()

    if rel:
        cv2.imwrite(os.path.join('.', "cutout" + str(counter) + ".jpg"), frame)
        counter = counter + 1
        cv2.imshow('frame', frame)
        cv2.waitKey(100)
    print("Number of frames", str(counter))
    
video.release()
cv2.destroyAllWindows()
"""

"""import os
import cv2

video_path = os.path.join(".", "wife.mp4")
video = cv2.VideoCapture(video_path)
print(type(video))

ret = True
while ret:
    ret, frame = video.read()

    if ret:
        cv2.imshow('frame', frame)
        cv2.waitKey(40)
    
video.release()
cv2.destroyAllWindows()
"""
"""import cv2
import os

img_path = os.path.join(".", "image.jpg")
image = cv2.imread(img_path)


new_image = cv2.imwrite(os.path.join(".", "new_image.jpg"), image)
cv2.imshow('image', image)
cv2.imshow('new_image', new_image)

cv2.waitKey(0)
"""