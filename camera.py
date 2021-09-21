import cv2                          # OpenCV to capture the frames from webcam was imported
import numpy                        # Numpy was imported to perform numerical calculations
from flask import Flask, render_template, Response, stream_with_context, request
# Flask webserver was imported, to upload the frames or video onto the webserver

video = cv2.VideoCapture(0)
# webcam capture started
app = Flask('__name__')
# Flask webserver initiallised and started

def video_stream():
# Method defined 
    while True:
    # infinite loop
        ret, frame = video.read()
        # frame captured one by one
        if not ret:
        # if no frame then break out of the loop
            break;
        else:
            ret, buffer = cv2.imencode('.jpeg',frame)
            # frame converted to JPEG format
            frame = buffer.tobytes()
            # JPEG format to bytes 
            yield (b' --frame\r\n' b'Content-type: image/jpeg\r\n\r\n' + frame +b'\r\n')
            # the bytes are broadcasted using yield function over HTTP protocol


# Context paths initiallised             
@app.route('/camera')
def camera():
    return render_template('camera.html')

@app.route('/video_feed')
def video_feed():
    return Response(video_stream(), mimetype='multipart/x-mixed-replace; boundary=frame')

app.run(host='localhost', port='5000', debug=False)
# running the flask webserver with port 5000
