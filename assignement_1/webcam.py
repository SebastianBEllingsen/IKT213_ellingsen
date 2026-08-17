import cv2
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
out_path = os.path.join(script_dir, "solutions", "camera_outputs.txt")


def save_cam_info(fps, frame_height, frame_width, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        f.write(f"FPS: {fps}\n")
        f.write(f"Frame Height: {frame_height}\n")
        f.write(f"Frame Width: {frame_width}\n")

cam = cv2.VideoCapture(0)
if not cam.isOpened():
    print("Failed to open camera.")
    exit(1)

frame_width = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cam.get(cv2.CAP_PROP_FPS))

try:
    while True:
        ret, frame = cam.read()
        if not ret:
            print("Failed to grab frame.")
            break

        cv2.imshow('Camera', frame)

        if cv2.waitKey(1) == ord('q'):
            break
finally:
    save_cam_info(fps, frame_height, frame_width, out_path)
    cam.release()
    cv2.destroyAllWindows()