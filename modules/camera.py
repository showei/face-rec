import cv2

from modules.face_detection import FaceDetector

class VideoCamera(object):
    def __init__(self):

        self.video = cv2.VideoCapture(0)
        # self.video = cv2.VideoCapture('video.mp4')
        self.face_detector = FaceDetector()
        fn_haar = 'haarcascade_frontalface_default.xml'
        self.haar_cascade = cv2.CascadeClassifier(fn_haar)
    def __del__(self):
        self.video.release()

    def get_frame(self):
        rval = False
        while (not rval):
            rval, image = self.video.read()
            if (not rval):
                print("Failed to open webcam. Trying again...")

        image, names = self.face_detector.draw_faces(image)

        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes(), names
