import cv2, time, pandas
from datetime import datetime

first_frame = None
status_list = [None,None]
time =[]
df = pandas.DataFrame(columnd=["start", "end"])

video = cv2.VideoCapture(0)

while True:
    check, frame = video.read()
    status = 0
    gray = cv2.cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussinBlur(gray, (21, 21), 0)

    if first_frame is None:
        first_frame = gray
        continue
