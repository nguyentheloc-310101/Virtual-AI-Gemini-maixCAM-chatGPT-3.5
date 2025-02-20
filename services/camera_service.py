# services/camera_service.py
import cv2
from config import CAMERA_INDEX


class CameraService:
    def __init__(self):
        self.cap = cv2.VideoCapture(CAMERA_INDEX)
        if not self.cap.isOpened():
            raise Exception("Error: Could not open video stream.")

    def get_frame(self):
        ret, frame = self.cap.read()
        if not ret:
            raise Exception("Failed to grab frame from camera.")
        return frame

    def release(self):
        self.cap.release()
        cv2.destroyAllWindows()

    def show_frame(self, frame):
        cv2.imshow("Fall Detection", frame)
