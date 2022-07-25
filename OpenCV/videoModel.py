#!/bin/env python3
# *-* utf-8 *-*
import numpy as np
import cv2
import time
# Code principal.
ttime = 0.0
cap = cv2.VideoCapture(0)
while(True):
  t0 = time.process_time()
  ret, frame = cap.read()
  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  x=np.shape(frame)[0]
  y=np.shape(frame)[1]
  c=np.shape(frame)[2]
  txt0 = "Dims : {0}x{1}x{2}".format(x,y,c)
  txt1 = "Temps : {0}s".format(ttime)
  txt2 = "Date : " + time.strftime("%H:%M\'%S\"")
  font = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
  cv2.putText(gray, txt0, (10,410), font, 1,(255,255,255) ,2 ,cv2.LINE_AA)
  cv2.putText(gray, txt1, (10,440), font, 1,(255,255,255) ,2 ,cv2.LINE_AA)
  cv2.putText(gray, txt2, (10,470), font, 1,(255,255,255) ,2 ,cv2.LINE_AA)
  cv2.imshow('video', gray)
  if (cv2.waitKey(1) & 0xFF == ord('q')) :
    break
  t1 = time.process_time()
  ttime = t1 - t0
  time.sleep(1.0)
cap.release()
cv2.destroyAllWindows()