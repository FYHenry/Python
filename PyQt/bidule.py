#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 14:02:21 2017

@author: fh
"""
##########
# BROKEN #
##########
import numpy as np
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QGridLayout, QLabel, QLineEdit, QCheckBox, QGroupBox
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
class Bidule(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("Le bidule")#Titre de boîte
        self.resize(250,250)#Taille de boîte
        self.boite=QVBoxLayout()#Boîte verticale
        self.fig = Figure()#Créer une figure.
        self.axes1 = self.fig.add_subplot(121)#Figure1
        self.axes2=self.fig.add_subplot(122)#Figure2
        self.x1=np.linspace(-np.pi,np.pi)
        self.x2=np.linspace(1,100)
        self.y1=np.cos(self.x1)**2-np.sin(self.x1)
        self.y2=np.exp(-self.x2**2)
        self.line1,=self.axes1.plot(self.x1,self.y1)
        self.line2,=self.axes2.plot(self.x2,self.y2)
        self.canvas=FigureCanvas(self.fig)#Toile portant la figure de Matplotlib.
        self.layout.addWidget(self.canvas)
        self.setLayout(self.boite)#Placer boîte
        self.soustitre=QLabel("Boîte à bouttons")#Sous-titre de sous-boîte
        self.soustitre.setMaximumSize(200,15)#Taille de sous-titre
        self.boite.addWidget(self.soustitre)#Placer sous-titre
        self.sousboite=QGridLayout()#Sous-boîte en matrice pour les bouttons
        self.boite.addLayout(self.sousboite)#Placer sous-boîte
        self.bouttons=[]#Liste des bouttons vide
        self.numeros=[]#Liste des numéros vide
        self.appuyer=[]
        for l in range(5):
            self.bouttons+=[[]]#Lignes de bouttons
            self.numeros+=[[]]#Lignes de numéros
            self.appuyer+=[[]]
            for c in range(5):
                self.bouttons[l]+=[QPushButton()]#Colonnes de bouttons
                self.numeros[l]+=["{}{}".format(l,c)]#Colonnes de numéros
                self.appuyer[l]+=[np.sin]
                self.bouttons[l][c].setMaximumSize(30,30)#Taille des bouttons
                self.bouttons[l][c].setText(self.numeros[l][c])#Numéros des bouttons
                self.sousboite.addWidget(self.bouttons[l][c],l,c)#Placer tous les bouttons
                def appui():
                    if self.bouttons[l][c].clicked!=QPushButton.clicked:
                        if self.numeros[l][c] == self.bouttons[l][c].text():
                            self.bouttons[l][c].setText("["+self.numeros[l][c]+"]")
                        else:
                            self.bouttons[l][c].setText(self.numeros[l][c])
                self.appuyer[l][c]=appui
                self.bouttons[l][c].clicked.connect(self.appuyer[l][c])#Connection entre bouttons et "appuyer"
        self.show()#Afficher.
'''
    def appuyer(self):
        n=self.numeros
        t=[]
        for l in range(len(self.bouttons)):
            t+=[[]]
            for c in range(len(self.bouttons[0])):
                t[l]+=[self.bouttons[l][c].text()]
        for l in range(len(self.bouttons)):
            for c in range(len(self.bouttons[0])):
                if self.bouttons[l][c].clicked==QPushButton.clicked:
                    if n[l][c]==t[l][c]:
                        self.bouttons[l][c].setText("["+n[l][c]+"]")
                    else:
                        self.bouttons[l][c].setText(n[l][c])
'''

def ouvrirBidule():
    app = QApplication.instance()
    if not app:
        app = QApplication(sys.argv)
    objet = Bidule()
    objet.show()
    app.exec_()

ouvrirBidule()
