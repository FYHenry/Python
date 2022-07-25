#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 15:46:23 2019

@author: fh
"""
import numpy as np
import matplotlib.pyplot as plt
import cv2

print("Que la fête commence !")
# Capture vidéo.
cap = cv2.VideoCapture(0)
plt.figure("Fenetre", figsize=[20,15], facecolor='grey')
# Début de boucle des images.
for i in range(20) :
  if not cap.isOpened():
    print("Erreur : N'a trouvé ni caméra, ni fichier vidéo.")
    break
  # Code de sortie et images de caméra.
  ret, frame = cap.read()
  if not ret :
    print("Erreur : On ne peut pas capturer d'images.")
  # Image convertie en NdG. Une moyenne des couleurs?
  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  # Affichage
  # Gris.
  plt.subplot(221)
  plt.title("Gris")
  plt.ylabel("X")
  plt.xlabel("Y")
  plt.imshow(gray, cmap='Greys_r')
  # Cyan
  plt.subplot(222)
  plt.title("Cyan")
  plt.ylabel("X")
  plt.xlabel("Y")
  plt.imshow(frame[:,:,0], cmap='Greys_r')
  # Vert
  plt.subplot(223)
  plt.title("Vert")
  plt.ylabel("X")
  plt.xlabel("Y")
  plt.imshow(frame[:,:,1], cmap='Greys_r')
  # Magenta
  plt.subplot(224)
  plt.title("Magenta")
  plt.ylabel("X")
  plt.xlabel("Y")
  plt.imshow(frame[:,:,2], cmap='Greys_r')
  # Pause.
  plt.pause(0.05)
  plt.clf()
  # Attente d'une touche pour terminer.
  if plt.waitforbuttonpress(timeout=0.1) :
    break
  if cv2.waitKey(1) & 0xFF == ord('q') :
    break
# Fin de capture.
plt.close('all')
cap.release()
# Fin des fenêtres.
cv2.destroyAllWindows()