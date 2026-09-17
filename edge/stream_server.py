from flask import Flask
from picamera2 import Picamera2
from io import BytesIO
from flask import Flask, Response

app = Flask(__name__)

picam2 = Picamera2()
picam2.start()                # start the camera (from camera_test.py)

def generate_frames():
    while True:
        stream = BytesIO()
        picam2.capture_file(stream, format='jpeg')
        stream.seek(0)
        frame_bytes = stream.read()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/')
def index():
    return "Hello from the robotf!"

app.run(host='0.0.0.0', port=5000)

