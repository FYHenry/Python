#!/bin/env python3
# *-* utf-8 *-*
import numpy as np
import matplotlib.pyplot as plt
import cv2
import time
# Code principal.
cap = cv2.VideoCapture(0)
ret, frame = cap.read()
[xl, yl, cl] = np.shape(frame)
red = np.ones([xl, yl, cl])
green = np.ones([xl, yl, cl])
blue = np.ones([xl, yl, cl])
while(True):
  ret, frame = cap.read()
  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  hist = cv2.calcHist([gray],[0],None,[256],[0,256])
  plt.plot(np.linspace(0,255,256),hist.T[0])
  plt.imshow('video', hist)
  if (cv2.waitKey(1) & 0xFF == ord('q')) :
    break
  time.sleep(1)
cap.release()
cv2.destroyAllWindows()
