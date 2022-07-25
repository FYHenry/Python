#!/bin/env python3
# *-* utf-8 *-*
import numpy as np
import cv2

# Fonction de seuillage.
def seuilRouge(gris, seuil=127):
  x=np.shape(frame)[0]
  y=np.shape(frame)[1]
  rouge = np.zeros([x,y,3])
  for i in range(0,x) :
    for j in range(0,y) :
      if not gris[i][j]<=seuil :
        rouge[i][j][2] = 200
  return rouge
def seuilAlt(gris, seuil=127):
  rouge, arbre = cv2.findContours(gris, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
  return rouge
# Code principal.
cap = cv2.VideoCapture(0)
while(True):
  ret, frame = cap.read()
  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  x=np.shape(frame)[0]
  y=np.shape(frame)[1]
  c=np.shape(frame)[2]
  red = seuilAlt(gray,24)
  txt0 = "Dims : {0}x{1}x{2}".format(x,y,c)
  font = cv2.FONT_HERSHEY_SIMPLEX
  cv2.putText(gray, txt0, (10,450), font, 1,(255,255,255) ,2 ,cv2.LINE_AA)
  cv2.drawContours(gray, red, -1, [0,0,200])
  cv2.imshow('video', gray)
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break
cap.release()
cv2.destroyAllWindows()
