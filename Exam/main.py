# Source - https://stackoverflow.com/a/34588758
# Posted by derricw, modified by community. See post 'Timeline' for change history
# Retrieved 2026-09-07, License - CC BY-SA 4.0

import cv2

def click_event(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, y)
        #need to save pt1, pt2 and pt3
        font = cv2.FONT_HERSHEY_SIMPLEX
        #doesnt show on the cam feed is ok
        cv2.putText(frame, f"{x},{y}", (x, y), font, 1, (255, 0, 0), 2)
        cv2.line(frame, (x, y), (x, y), (0, 0, 255), 5)
    if event == cv2.EVENT_RBUTTONDOWN:
        print(x, y)
        font = cv2.FONT_HERSHEY_SIMPLEX
        b, g, r = frame[y, x]
        cv2.putText(frame, f"{b},{g},{r}", (x, y), font, 0.5, (255, 255, 0), 2)
        #New frame showing pixel cord on image
        #return the pixel cords to video
        cv2.imshow('image', frame)
cam = cv2.VideoCapture(0)

cv2.namedWindow("Mosaic")

img_counter = 0
lbtn_click_counter = 0
while True:
    ret, frame = cam.read()
    if not ret:
        print("failed to grab frame")
        break
    cv2.imshow("Mosaic", frame)

    cv2.setMouseCallback("Mosaic", click_event)

    k = cv2.waitKey(1)
    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        # SPACE pressed
        img_name = "opencv_frame_{}.png".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        img_counter += 1

cam.release()

cv2.destroyAllWindows()
