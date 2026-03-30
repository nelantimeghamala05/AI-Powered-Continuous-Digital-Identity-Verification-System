import cv2
import time

def capture_frame():
    cam = cv2.VideoCapture(0)
    time.sleep(2)  # allow camera to adjust

    for _ in range(5):
        ret, frame = cam.read()

    cam.release()

    if not ret:
        raise Exception("Camera not accessible")

    return frame