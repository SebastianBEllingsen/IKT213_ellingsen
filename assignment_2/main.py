import cv2
import numpy as np
img1 = cv2.imread("iris-1.png")

def padding(image, border_width):
    return cv2.copyMakeBorder(image, border_width, border_width, border_width, border_width, cv2.BORDER_REFLECT)

def cropping(image, x_0, x_1, y_0, y_1):
    return image[x_0:x_1, y_0:y_1]

def rezise(image, width, height):
    return cv2.resize(image, (width, height))

def copy(image, emptyPictureArray):
    height, width, channels = image.shape
    for y in range(height):
        for x in range(width):
            for c in range(channels):
                emptyPictureArray[y, x, c] = image[y, x, c]
    return emptyPictureArray

def grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def hsv(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

def hue_shifted(image, emptyPictureArray, hue):
    height, width, channel = image.shape

    for y in range(height):
        for x in range(width):
            for c in range(channel):
                emptyPictureArray[y, x, c] = np.uint8(image[y, x, c] + hue)
    return emptyPictureArray

def smoothing(image):
    return cv2.GaussianBlur(image, (15, 15), 0, borderType=cv2.BORDER_DEFAULT)

def rotation(image, rotation_angle):
    if rotation_angle == 90:
        return cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
    elif rotation_angle == 180:
        return cv2.rotate(image, cv2.ROTATE_180)
    else:
        return image

#1 Padding
cv2.imwrite('iris-1-padded.png', padding(img1, 100))

#2 Cropping
image_shape = img1.shape
print(image_shape[0])
print(image_shape[1])
print(image_shape[2])
cv2.imwrite('iris-1-cropped.png', cropping(img1, 200, image_shape[0]-130, 200, image_shape[1]-130))

#3 Resizing
cv2.imwrite('iris-1-resized.png', rezise(img1, 200, 200))

#4 Copying
height, width, channels = img1.shape
emptyPictureArray = np.zeros((height, width, 3), dtype=np.uint8)
cv2.imwrite("copied_iris.png", copy(img1, emptyPictureArray))

#5 Grayscale
cv2.imwrite("grayscale_iris.png", grayscale(img1))

#6HSV
cv2.imwrite("hsv_iris.png", hsv(img1))

#7 Color Shitfing
emptyPictureArray = np.zeros((height, width, 3), dtype=np.uint8)
cv2.imwrite("hue_shifted_iris.png", hue_shifted(img1, emptyPictureArray, 50))

#8 Smoothing
cv2.imwrite("smoothing_iris.png", smoothing(img1))

#9 Rotation
cv2.imwrite("rotation_iris.png", rotation(img1, 180))