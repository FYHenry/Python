#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 18:20:31 2019

@author: fh
"""
import numpy as np
import matplotlib.pyplot as plt
import cv2

cap = cv2.VideoCapture(0)
ret, frame = cap.read()
L=np.size(frame[:,0,0])
C=np.size(frame[0,:,0])
col=np.size(frame[0,0,:])
print("Lignes : ",L)
print("Colonnes : ",C)
print("Canaux : ",col)

while(True):
  # Capture frame-by-frame
  ret, frame = cap.read()
  # Our operations on the frame come here
  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  sobel = cv2.Sobel(gray,cv2.CV_8U,1,0,ksize=3)
  hist = cv2.calcHist([gray],[0],None,[256],[0,256])
  # Display the resulting frame
  cv2.imshow('Coloré',frame)
  cv2.imshow('Gris',gray)
  cv2.imshow("Sobel",sobel)
  cv2.destroyAllWindows()
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break
# When everything done, release the capture
cap.release()
print("Lignes : ",np.size(hist[:,0]))
print("Colonnes : ",np.size(hist[0,:]))
print("Canaux : ",np.size(hist[0,0]))
plt.plot(np.linspace(10,255,246),hist[10:,0])
plt.title("Histogramme total\nTaille d'image : {}x{}".format(L,C))
plt.xlim([10,255])
plt.show()
