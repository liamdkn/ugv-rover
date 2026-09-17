from picamera2 import Picamera2

picam2 = Picamera2()
picam2.start()
picam2.capture_file("test.jpg")

from picamera2 import Picamera2
from io import BytesIO
picam2 = Picamera2()
picam2.start()  # start it (remember from your very first camera script)

def generate_frames():
    while True:
        stream = BytesIO()
        picam2.capture_file(stream, format='jpeg')
        stream.seek(0)
        frame_bytes = stream.read()