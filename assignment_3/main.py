import cv2
import numpy as np


def sobel_edge_detection(image):
    image_blur = cv2.GaussianBlur(image, (3, 3), 0)
    sobel_xy = cv2.Sobel(image_blur, cv2.CV_64F, 1, 1, ksize=1)
    sobel_xy = cv2.normalize(sobel_xy, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)
    cv2.imwrite("sobel_edge_detected.png", sobel_xy)
    return sobel_xy

def canny_edge_detection(image, threshold_1, threshold_2):
    image_blur = cv2.GaussianBlur(image, (3, 3), 0)
    canny_edge = cv2.Canny(image_blur, threshold_1, threshold_2)
    return canny_edge

#LES MER HER
def template_match(image, template):

    threshold = 0.9

    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

    h, w = template_gray.shape[:2]

    res = cv2.matchTemplate(img_gray, template_gray, cv2.TM_CCOEFF_NORMED)
    loc = np.where(res >= threshold)

    for pt in zip(*loc[::-1]):  # loc is (row, col) -> swap to (x, y)
        cv2.rectangle(image, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)

    cv2.imwrite("template_match_result.png", image)
    return image

def resize(image, scale_factor:int, up_or_down:str):
    result = image
    for _ in range (scale_factor):
        result = cv2.pyrUp(result) if up_or_down == "up" else cv2.pyrDown(result)
    cv2.imwrite("resized_image.png", result)
    return result



img1 = cv2.imread("lambo.png")

shapes = cv2.imread("shapes-1.png")
shapes_template = cv2.imread("shapes_template.jpg")




#cv2.imshow("image", shapes)
#cv2.imshow("image", shapes_template)
#cv2.waitKey(0)
#cv2.destroyAllWindows()


#cv2.imshow("image", img1)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

cv2.imwrite("sobel_edge_detected.png", sobel_edge_detection(img1))

cv2.imwrite("canny_edge_detected.png", canny_edge_detection(img1, 50, 50))

template_match(shapes, shapes_template)

resize(img1, 2, "up")