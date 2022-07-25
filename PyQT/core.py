#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 15:25:01 2018

@author: fh
"""

from PyQt5.QtWidgets import QWidget, QApplication, QGridLayout, QPushButton

class Fenestre(QWidget):# Fenêtre finale affichée.
    def __init__(self):# Constructeur.
        QWidget.__init__(self)# Import des propriétés de QWidget.
        self.setWindowTitle("Cases Voisines")# Insertion de titre de fenêtre.
        self.resize(200, 200)#Taille de la fenêtre : x et y.
        self.layout = QGridLayout()# Grille de bouttons.
        self.layout.setColumnStretch(80, 80)
        self.layout.setRowStretch(80, 80)
        for i in range(5):# Par lignes.
            for j in range(5):# Par colonnes.
                self.buttonCase = QPushButton("x")# Nouveau boutton.
                self.buttonCase.setMaximumSize(40, 40)# Dimensions du boutton.
                self.layout.addWidget(self.buttonCase, i, j)# Insertion du boutton.
        self.setLayout(self.layout)# Insertion de la grille.
        self.showNormal()# Afficher.
        
def execution():# Exécuter une fois.
    import sys
    app = QApplication.instance() 
    if not app:
        app = QApplication(sys.argv)
    fen = Fenestre()
    fen.show()
    app.exec_()