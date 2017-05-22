import cv2
import os


class FaceRecognizer(object):
    def __init__(self):
        self.model = cv2.face.createFisherFaceRecognizer()
        self.model.load('fisher.model')

        fn_dir = 'att_faces'
        (self.names, id) = ({}, 0)

        for (subdirs, dirs, files) in os.walk(fn_dir):

            for subdir in dirs:
                self.names[id] = subdir
                id += 1

    def identify_face(self, face):
        face_resize = cv2.resize(face, (299, 299))
        prediction = self.model.predict(face_resize)
        if prediction[1] < 1900:
            return self.names[prediction[0]]
        else:
            return None

