import cv2
from modules.face_recognition import FaceRecognizer

class FaceDetector(object):
    def __init__(self):
        fn_haar = 'haarcascade_frontalface_default.xml'
        self.haar_cascade = cv2.CascadeClassifier(fn_haar)
        self.face_identifier = FaceRecognizer().identify_face

    def get_faces(self, img):
        faces = self.haar_cascade.detectMultiScale(img)
        return faces


    def draw_faces(self, img):
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = self.get_faces(gray)
        for face_co in faces:
            (x, y, w, h) = [v for v in face_co]
            face = gray[y:y + h, x:x + w]
            name = self.face_identifier(face)
            if name:
                cv2.putText(img, '%s' % name,
                            (x - 10, y - 10), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0))
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
        return img
