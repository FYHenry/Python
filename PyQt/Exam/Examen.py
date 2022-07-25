#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 09:45:30 2017

@author: fh

Examen de David Cassagne.
"""

import numpy as np
import matplotlib.pyplot as plt
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QLineEdit, QCheckBox, QGroupBox
from PyQt5.QtCore import Qt
"""
Interface graphique - dipositif de sécurité à 4 cases
"""
class Digicode(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("Digicode")
        self.resize(250,250)
        self.layout=QVBoxLayout()#Mettre en forme.
        self.setLayout(self.layout)
        
        self.cocheA=QCheckBox("A")
        self.cocheA.clicked.connect(self.set_affiche)
        self.layout.addWidget(self.cocheA)
        self.cocheB=QCheckBox("B")
        self.cocheB.clicked.connect(self.set_affiche)
        self.layout.addWidget(self.cocheB)
        self.cocheC=QCheckBox("C")
        self.cocheC.clicked.connect(self.set_affiche)
        self.layout.addWidget(self.cocheC)
        self.cocheD=QCheckBox("D")
        self.cocheD.clicked.connect(self.set_affiche)
        self.layout.addWidget(self.cocheD)
        
        self.affiche=QLabel("Affiche: Éteint")
        self.layout.addWidget(self.affiche)
    def set_affiche(self):
        a=self.cocheA.checkState()
        b=self.cocheB.checkState()
        c=self.cocheC.checkState()
        d=self.cocheD.checkState()
        oui=Qt.Checked; non=Qt.Unchecked
        if a==oui and b==non and c==oui and d==non:
            self.affiche.setText("Affiche: Allumé")
        else:
            self.affiche.setText("Affiche: Éteint")
        
def ctrlfenDigicode():
	# Premiere etape : creation d'une application Qt avec QApplication
	#    afin d'avoir un fonctionnement correct avec IDLE ou Canopy
	#    on verifie s'il existe deja une instance de QApplication
	app = QApplication.instance() 
	if not app: # sinon on cree une instance de QApplication
	    app = QApplication(sys.argv)
	# creation d'une fenetre avec QWidget dont on place la reference dans fen
	fen = Digicode()	
	# la fenetre est rendue visible
	fen.show()	
	# execution de l'application, l'execution permet de gerer les evenements
	app.exec_()
#ctrlfenDigicode()
"""
Gestion d'un mois et d'une année
"""
class Calendrier(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("Calendrier")
        self.resize(250,250)
        self.layout=QVBoxLayout()#Mettre en forme.
        self.setLayout(self.layout)
        
        self.champ_mois=QLabel("Mois : 01")
        self.layout.addWidget(self.champ_mois)

        self.mmois=QPushButton("-mois")
        self.mmois.clicked.connect(self.set_mmois)
        self.layout.addWidget(self.mmois)
        
        self.pmois=QPushButton("+mois")
        self.pmois.clicked.connect(self.set_pmois)
        self.layout.addWidget(self.pmois)
        
        self.champ_annee=QLabel("Année : 2015")
        self.layout.addWidget(self.champ_annee)
        
        self.mannee=QPushButton("-année")
        self.mannee.clicked.connect(self.set_mannee)
        self.layout.addWidget(self.mannee)
        
        self.pannee=QPushButton("+année")
        self.pannee.clicked.connect(self.set_pannee)
        self.layout.addWidget(self.pannee)
        
        self.avance=QCheckBox("Avance Rapide")
        self.avance.clicked.connect(self.rapide)
        self.layout.addWidget(self.avance)
        
    def set_mmois(self):
        mois=self.champ_mois.text()
        m=int(mois[7:9])
        annee=self.champ_annee.text()
        a=int(annee[8:12])
        if m==1:
            self.champ_mois.setText("Mois : 12")
            self.champ_annee.setText("Année : {}".format(a-1))
        else:
            self.champ_mois.setText("Mois : {}".format(str(m-1).zfill(2)))

    def set_pmois(self):
        mois=self.champ_mois.text()
        m=int(mois[7:9])
        annee=self.champ_annee.text()
        a=int(annee[8:12])
        if m==12:
            self.champ_mois.setText("Mois : 01")
            self.champ_annee.setText("Année : {}".format(a+1))
        else:
            self.champ_mois.setText("Mois : {}".format(str(m+1).zfill(2)))

    def set_mannee(self):
        annee=self.champ_annee.text()
        a=int(annee[8:12])
        self.champ_annee.setText("Année : {}".format(str(a-1).zfill(4)))

    def set_pannee(self):
        annee=self.champ_annee.text()
        a=int(annee[8:12])
        self.champ_annee.setText("Année : {}".format(str(a+1).zfill(4)))

    def rapide(self):
        c=self.avance.checkState()
        oui=Qt.Checked; non=Qt.Unchecked
        if c==oui:
            self.mmois.clicked.disconnect(self.set_mmois)
            self.pmois.clicked.disconnect(self.set_pmois)
            self.pannee.clicked.disconnect(self.set_pannee)
            self.mannee.clicked.disconnect(self.set_mannee)
            self.mmois.clicked.connect(self.set_rmmois)
            self.pmois.clicked.connect(self.set_rpmois)
            self.pannee.clicked.connect(self.set_rpannee)
            self.mannee.clicked.connect(self.set_rmannee)
        elif c==non:
            self.mmois.clicked.disconnect(self.set_rmmois)
            self.pmois.clicked.disconnect(self.set_rpmois)
            self.pannee.clicked.disconnect(self.set_rpannee)
            self.mannee.clicked.disconnect(self.set_rmannee)
            self.mmois.clicked.connect(self.set_mmois)
            self.pmois.clicked.connect(self.set_pmois)
            self.pannee.clicked.connect(self.set_pannee)
            self.mannee.clicked.connect(self.set_mannee)

    def set_rmmois(self):
        mois=self.champ_mois.text()
        m=int(mois[7:9])
        annee=self.champ_annee.text()
        a=int(annee[8:12])
        if m==1:
            self.champ_mois.setText("Mois : 10")
            self.champ_annee.setText("Année : {}".format(a-1))
        elif m==2:
            self.champ_mois.setText("Mois : 11")
            self.champ_annee.setText("Année : {}".format(a-1))
        elif m==3:
            self.champ_mois.setText("Mois : 12")
            self.champ_annee.setText("Année : {}".format(a-1))
        else:
            self.champ_mois.setText("Mois : {}".format(str(m-3).zfill(2)))
    
    def set_rpmois(self):
        mois=self.champ_mois.text()
        m=int(mois[7:9])
        annee=self.champ_annee.text()
        a=int(annee[8:12])
        if m==10:
            self.champ_mois.setText("Mois : 01")
            self.champ_annee.setText("Année : {}".format(a+1))
        elif m==11:
            self.champ_mois.setText("Mois : 02")
            self.champ_annee.setText("Année : {}".format(a+1))
        elif m==12:
            self.champ_mois.setText("Mois : 03")
            self.champ_annee.setText("Année : {}".format(a+1))
        else:
            self.champ_mois.setText("Mois : {}".format(str(m+2).zfill(2)))

    def set_rmannee(self):
        annee=self.champ_annee.text()
        a=int(annee[8:12])
        self.champ_annee.setText("Année : {}".format(str(a-10).zfill(4)))
    
    def set_rpannee(self):
        annee=self.champ_annee.text()
        a=int(annee[8:12])
        self.champ_annee.setText("Année : {}".format(str(a+10).zfill(4)))
def ctrlfenCalendrier():
	# Premiere etape : creation d'une application Qt avec QApplication
	#    afin d'avoir un fonctionnement correct avec IDLE ou Canopy
	#    on verifie s'il existe deja une instance de QApplication
	app = QApplication.instance() 
	if not app: # sinon on cree une instance de QApplication
	    app = QApplication(sys.argv)
	# creation d'une fenetre avec QWidget dont on place la reference dans fen
	fen = Calendrier()	
	# la fenetre est rendue visible
	fen.show()	
	# execution de l'application, l'execution permet de gerer les evenements
	app.exec_()
#ctrlfenCalendrier()

"""
Interface graphique - Echange de messages entre trois fenêtres(Cassé)
"""

class Chat0(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.nom="vide"
        self.vsn0=self
        self.vsn1=self
        self.setWindowTitle(self.nom)
        self.resize(250,250)
        self.layout=QVBoxLayout()#Mettre en forme.
        self.setLayout(self.layout)
        
        self.texto=QLabel("texto")
        self.layout.addWidget(self.texto)
        
        self.redac=QLineEdit("Tape ici.")
        self.layout.addWidget(self.redac)
        
        self.groupe=QGroupBox("Boîte à bouttons")
        self.groupe_layout=QVBoxLayout(self.groupe)
        self.setLayout(self.groupe_layout)
        self.layout.addWidget(self.groupe)
        
        self.valide0=QPushButton("Envoi {}".format(self.vsn0.nom))
        self.valide0.clicked.connect(self.envoi0)
        self.groupe_layout.addWidget(self.valide0)
        
        self.valide1=QPushButton("Envoi {}".format(self.vsn1.nom))
        self.valide1.clicked.connect(self.envoi1)
        self.groupe_layout.addWidget(self.valide1)
        
    def envoi0(self):
        txt=self.redac.text()
        txt0=self.vsn0.texto.text()
        self.vsn0.texto.setText(txt0+"\n"+txt)
    
    def envoi1(self):
        txt=self.redac.text()
        txt0=self.vsn1.texto.text()
        self.vsn1.texto.setText(txt0+"\n"+txt)

class Chat(QWidget):
    def __init__(self,user,v0,v1):
        QWidget.__init__(self)
        self.nom=user
        self.vsn0=v0
        self.vsn1=v1
        self.setWindowTitle(self.nom)
        self.resize(250,250)
        self.layout=QVBoxLayout()#Mettre en forme.
        self.setLayout(self.layout)
        
        self.texto=QLabel("texto")
        self.layout.addWidget(self.texto)
        
        self.redac=QLineEdit("Tape ici.")
        self.layout.addWidget(self.redac)
        
        self.groupe=QGroupBox("Boîte à bouttons")
        self.groupe_layout=QVBoxLayout(self.groupe)
        self.setLayout(self.groupe_layout)
        self.layout.addWidget(self.groupe)
        
        self.valide0=QPushButton("Envoi {}".format(self.vsn0.nom))
        self.valide0.clicked.connect(self.envoi0)
        self.groupe_layout.addWidget(self.valide0)
        
        self.valide1=QPushButton("Envoi {}".format(self.vsn1.nom))
        self.valide1.clicked.connect(self.envoi1)
        self.groupe_layout.addWidget(self.valide1)
        
    def envoi0(self):
        txt=self.redac.text()
        txt0=self.vsn0.texto.text()
        self.vsn0.texto.setText(txt0+"\n"+txt)
    
    def envoi1(self):
        txt=self.redac.text()
        txt0=self.vsn1.texto.text()
        self.vsn1.texto.setText(txt0+"\n"+txt)
     
def ctrlfenChat():
	# Premiere etape : creation d'une application Qt avec QApplication
	#    afin d'avoir un fonctionnement correct avec IDLE ou Canopy
	#    on verifie s'il existe deja une instance de QApplication
	app = QApplication.instance() 
	if not app: # sinon on cree une instance de QApplication
	    app = QApplication(sys.argv)
	# creation d'une fenetre avec QWidget dont on place la reference dans fen
	c0=Chat0();fenAlice=Chat("",c0,c0);fenEve=Chat("",c0,c0);fenBob=Chat("",c0,c0);fenAlice=Chat("Alice",fenBob,fenEve);fenBob=Chat("Bob",fenEve,fenAlice);fenEve=Chat("Ève",fenAlice,fenBob);fenAlice=Chat("Alice",fenBob,fenEve);fenBob=Chat("Bob",fenEve,fenAlice);fenEve=Chat("Ève",fenAlice,fenBob)
	# la fenetre est rendue visible
	fenAlice.show();fenBob.show();fenEve.show()
	# execution de l'application, l'execution permet de gerer les evenements
	app.exec_()
#ctrlfenChat()

class ChatOrigin(QWidget):
     def __init__(self,titre,Voisin0,Voisin1):
        QWidget.__init__(self)
        self.Voisin0=Voisin0
        self.Voisin1=Voisin1
        self.titre=titre
        
        self.setWindowTitle(self.titre)
        self.resize(250,250)
        self.layout=QVBoxLayout()
        self.setLayout(self.layout)
        
        self.lu=QLabel("Lis ici")
        self.layout.addWidget(self.lu)
        
        self.ecrit=QLineEdit("Tape ici.")
        self.layout.addWidget(self.ecrit)
        
        self.groupe=QGroupBox("Boîte à bouttons")
        self.groupe_layout=QVBoxLayout(self.groupe)
        self.setLayout(self.groupe_layout)
        self.layout.addWidget(self.groupe)
        
        self.envoyer0=QPushButton("Envoie à 0")
        self.envoyer0.clicked.connect(self.Voisin0)
        self.groupe_layout.addWidget(self.envoyer0)
        
        self.envoyer1=QPushButton("Envoie à 1")
        self.envoyer1.clicked.connect(self.Voisin1)
        self.groupe_layout.addWidget(self.envoyer1)
        
    def envoi0(self):
        recu=self.Voisin0.lu.text()
        emis=self.ecrit.text()
        self.Voisin0.lu.setText("{}\n{}".format(recu,emis))
        
    def envoi1(self):
        recu=self.Voisin1.lu.text()
        emis=self.ecrit.text()
        self.Voisin1.lu.setText("{}\n{}".format(recu,emis))
        
class Alice(ChatOrigin):
    def __init__(self):
        ChatOrigin.__init__(self)
        
def ctrlChatO():
    app = QApplication.instance() 
    if not app :
        app = QApplication(sys.argv)
    fen=ChatOrigin()
    fen.show()
    app.exec_()
ctrlChatO()
"""
Animation - Corpuscules dans une boîte
"""

def pointsBoite(vitesse=1,N=5):
    plt.plot([0,0,40,40,0],[0,40,40,0,0])
    v=np.zeros([2,N])
    r0=np.ones([2,N])*20
    for i in range(N):
        theta=np.random.rand()*2*np.pi
        v[0,i]=vitesse*np.cos(theta)
        v[1,i]=vitesse*np.sin(theta)
    for t in range(80):# Nombre d'itérations.
        r=t*v+r0
        for p in range(2):
            for q in range(N):
                r[p,q]=r[p,q]%40
        if t == 0:
            line, = plt.plot(r[0],r[1],"o",lw=3)
        else:
            line.set_xdata(r[0])
            line.set_ydata(r[1])
            plt.title("Temps : {}/{}".format(t,80-1))
        plt.pause(0.0005) # pause avec duree en secondes
    plt.show()
#pointsBoite(2,5)
"""
Animation d'orbite élliptique.
"""
def rellipse(t,e=1,omega=2*np.pi/10):
    return np.array([np.cos(omega*t),np.sin(omega*t)/e])
def orbite(e=1,omega=2*np.pi/10):
    T=np.linspace(0,1000,1001)
    R=rellipse(T,e,2*np.pi/1000)
    plt.plot(R[0],R[1],lw=2)
    for t in range(101):
        r=rellipse(t,e,omega)
        if t == 0:
            line, = plt.plot(r[0],r[1],"o",lw=10)
        else:
            line.set_xdata(r[0])
            line.set_ydata(r[1])
            plt.title("Temps : {}/{}".format(t,101-1))
        plt.pause(0.00005) # pause avec duree en secondes
    plt.show()
#orbite(2,2*np.pi/40)