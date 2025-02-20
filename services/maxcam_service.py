# services/maxcam_service.py
import cv2


class MaxcamService:
    def __init__(self, camera_index=0, resolution=(640, 480)):

        self.camera_index = camera_index
        self.resolution = resolution
        self.cap = cv2.VideoCapture(self.camera_index)

        # Set the camera resolution
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, self.resolution[0])
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.resolution[1])

        if not self.cap.isOpened():
            raise Exception("MaxcamService: Could not open maixCAM.")

    def get_frame(self):
        """
        Captures a single frame from the maixCAM.
        :return: The captured frame.
        """
        ret, frame = self.cap.read()
        if not ret:
            raise Exception(
                "MaxcamService: Failed to grab frame from maixCAM.")
        return frame

    def release(self):
        """
        Releases the camera and closes any OpenCV windows.
        """
        self.cap.release()
        cv2.destroyAllWindows()

    def show_frame(self, frame, window_name="maixCAM Frame"):
        cv2.imshow(window_name, frame)
