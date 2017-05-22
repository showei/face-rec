from flask import render_template, Response, Blueprint, redirect

from modules.camera import VideoCamera

blueprint = Blueprint('main', __name__, template_folder='templates')


@blueprint.route('/')
def home():
    return render_template('index.html')


def gen(camera):
    while True:
        frame, names = camera.get_frame()
        if not len(names):
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
        else:
            print(names)
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


@blueprint.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

