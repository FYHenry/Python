#!/env/bin python
# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Script pour faire une nuance de gris sinusoïdeale.
"""
from numpy import array,linspace,sin,ones,pi
import matplotlib.pyplot as plt
import matplotlib.colors as clr
image=ones([1000,1000])
for x in range(1,1000):
    image[x][:]=sin(x*2*pi/100)*ones([1000])
plt.figure()
plt.imshow(image,cmap='gray')
plt.title("Sinusoïde de NdG")
plt.pause(1.00)
