import cv2

def print_image_information(img):
    if img is None:
        print("Failed to load image. Check the file path.")
        return

    height, width = img.shape[:2]
    channels = img.shape[2] if len(img.shape) == 3 else 1

    print("Image height:", height)
    print("Image width:", width)
    print("Image channels:", channels)
    print("Image size (total pixels):", img.size)
    print("Image data type:", img.dtype)

img = cv2.imread("iris-1.jpg")

print_image_information(img)
