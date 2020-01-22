import cv2
import sys

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
video_capture = cv2.VideoCapture(0) 

while True:

    # Capturing frame by frame
    retval, frame = video_capture.read()

    # Converts image to grayscale and then converts it back to color in order to read better
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 

    # Features detected
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize= (35,35)
    )

    # Rectangle
    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (50,50,200), 2 )

    #Show Frame
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        sys.exit()