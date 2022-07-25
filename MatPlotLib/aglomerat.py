#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 23:36:50 2017

@author: fh

Simulation d'aglomération de particules
"""
def matrix_rand(L,C,d=0.10):
    from numpy import zeros
    from time import sleep
    from random import random as rand
    M=zeros([L,C],dtype=bool)
    for i in range(L):
        for j in range(C):
            r=rand()
            v=r<d
            M[i,j]=v
    return M
def aglo(M):
    from numpy import size,array,zeros
    L=size(M[:,0])
    C=size(M[0,:])
    #Poids.
    P=array([[[ 0, 0, 0, 0, 0],#Poids en ligne.
              [ 0,-1, 0, 1, 0],
              [-1,-2, 0, 2, 1],
              [ 0,-1, 0, 1, 0],
              [ 0, 0, 0, 0, 0]],
             [[ 0, 0, 1, 0, 0],#Poids en colonne.
              [ 0, 1, 2, 1, 0],
              [ 0, 0, 0, 0, 0],
              [ 0,-1,-2,-1, 0],
              [ 0, 0,-1, 0, 0]]],dtype=int)
    #Fenêtre.
    F=zeros([2,5,5],dtype=int)
    for i in range(L):
        for j in range(C):
            #Indices périodiques.
            SSl=(i-2)%L
            Sl=(i-1)%L
            l=i%L
            Nl=(i+1)%L
            NNl=(i+2)%L
            OOc=(j-2)%C
            Oc=(j-1)%C
            c=j%C
            Ec=(j+1)%C
            EEc=(j+2)%C
            #Fenêtre.
            #Ligne à l'ouest.
            F[0,1,1]=P[0,1,1]*M[Nl ,Oc ]
            F[0,2,0]=P[0,2,0]*M[l  ,OOc]
            F[0,2,1]=P[0,2,1]*M[l  ,Oc ]
            F[0,3,1]=P[0,3,1]*M[Sl ,Oc ]
            #Ligne à l'est.
            F[0,1,3]=P[0,1,3]*M[Nl ,Ec ]
            F[0,2,3]=P[0,2,3]*M[l  ,Ec ]
            F[0,2,4]=P[0,2,4]*M[l  ,EEc]
            F[0,3,3]=P[0,3,3]*M[Sl ,Ec ]
            #Colonne au nord.
            F[1,0,2]=P[1,0,2]*M[NNl,c  ]
            F[1,1,1]=P[1,1,1]*M[Nl ,Oc ]
            F[1,1,2]=P[1,1,2]*M[Nl ,c  ]
            F[1,1,3]=P[1,1,3]*M[Nl ,Ec ]
            #Colonne au sud.
            F[1,3,1]=P[1,3,1]*M[Sl ,Oc ]
            F[1,3,2]=P[1,3,2]*M[Sl ,c  ]
            F[1,3,3]=P[1,3,3]*M[Sl ,Ec ]
            F[1,4,2]=P[1,4,2]*M[SSl,c  ]
            #Force verticale.
            Fy=F[0].sum()
            #Force horizontale.
            Fx=F[1].sum()
            if   abs(Fy)>abs(Fx) and Fy>0 and (not M[Nl,c ]):#Au nord.
                #Centre->Nord.
                M[l,c],M[Nl,c ]=False,True
            elif abs(Fy)>abs(Fx) and Fy<0 and (not M[Sl,c ]):#Au sud.
                #Centre->Sud.
                M[l,c],M[Sl,c ]=False,True
            elif abs(Fx)>abs(Fy) and Fx>0 and (not M[l ,Ec]):#A l'est.
                #Centre->Est.
                M[l,c],M[l ,Ec]=False,True
            elif abs(Fx)>abs(Fy) and Fx<0 and (not M[l ,Oc]):#A l'ouest.
                #Centre->Ouest.
                M[l,c],M[l ,Oc]=False,True
    return M
def aglo_test():
    M=matrix_rand(20,20)
    M1=M
    for t in range(1):
        M1=aglo(M1)
    print(M*1)
    print(M1*1)
    print("Sommes :",M.sum()," et ",M1.sum(),".")
    print("M=M1 :\n",(M==M1)*1)
    print("Densité : ",M.sum()/M.size)
from matplotlib.pyplot import imshow,figure,pause,title
figure("Graphe")
for t in range(31):
    M=matrix_rand(200,200,0.8)
    imshow(M,cmap='gray',interpolation='nearest')
    ttr="Itération :{:d}".format(t)
    ttr+="\nDensité : {:03.1f}%".format(M.sum()*100/M.size)
    title(ttr)
    pause(0.99)