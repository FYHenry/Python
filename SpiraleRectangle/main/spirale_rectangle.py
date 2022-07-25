#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""


### Spirale rectangulaire

Ce petit tas de codes permet de simuler une spirale carrée en rotation.
Il a été créé pour *Spyder* 3.3.1, sous *Ubuntu* 16.04.5.

@organization: Alnotz Corp.
@author: Alnotz
@date: 02/09/2018
@version: 0.1
@copyright: GNU General Public License 3


"""
# Outils graphiques
from matplotlib.pyplot import figure, \
                              plot, \
                              pause, \
                              xlim, \
                              ylim, \
                              show, \
                              close, \
                              savefig
# Outils d'analyse numérique.
from numpy import array, sqrt, complex

# Racine du projet.
root = "projet_spirale_rectangle/"
# Données images en format PNG. Chez moi, de script s'exécute 
#depuis le répertoire `./main`.
data = "../data/"

a = 1#Coté.

# Suite complexe à construire. Retourne un vecteur complexe.
def suite():
    """
    
    #### Fonction suite
    
        Renvoie un tableau 1D de la suite complexe *droite*.
        Ce tableau permettra de trace la première spirale retangle.
    
    """
    z = complex(0,0)# Nombre complexe initial.
    Z = [z]# Début de suite.
    for n in range(0, 20):# Calcul récursif des termes suivants.
        z = z + complex(0, 1)**n * 2**(-n/2 + 1/2) * a
        Z = Z + [z]
    return array(Z)

# Construction des courbes, animation et enregistrement.
def graph():
    """
    
    #### Fonction graph
    
        Fonction principale.
        Elle cumule trois actions :
        * Construire les spirales rectangles *obliques*;
        * Illustrer la séquence d'images;
        * Enregistrer sous format PNG.
    
        À la fin, la fenêtre se ferme.
        
    """
    # C'est pour faire un joli texte interactif.
    from sys import stdout
    fig = figure("Graphe: aperçu")# Graphe à animer.
    N = 40# Nombre d'images: 40
    Z0 = suite()# Spirale rectangle "droite".
    print("", end="\n")
    for t in range(1*N + 1):# Animation sur 40 images PNG.
        fig.clf()# Graphe nettoyé.
        c1 = t/N
        c1 = c1 - int(c1)
        z = complex(0, (1-c1) * 2)
        Z = [z]# Construction de la prochaine spirale en 20 points.
        for n in range(0, 20):# Termes complexes de la spirale
        # "oblique".
            z = z + c1 * 2**((1-n) / 2) \
                * complex(0, 1)**n + (1-c1) * 2**((2-n) / 2) \
                * complex(0, 1)**(n-1)
            Z += [z]
        Z = array(Z)# Suite complexe de la spirale "oblique" finie.
        plot(Z0.real, Z0.imag, "k")# Spirale "droite" tracée.
        plot(Z.real, Z.imag, "r")# Spirale "oblique" tracée.
        xlim([0, sqrt(2) * a])# On limite à l'horizontale.
        ylim([0, a])# On limite à la verticale.
        stdout.write("\rImage {:03d}/{:03d}".format(t, N))
        show()# Affichage .
        file = data + "spirale{:03d}.png".format(t)# Les fichiers 
        #image ont des noms génériques du numéro 000 à 999.
        try:# On vérifie si le fichier existe déjà.
            o = open(file, mode='x')#Pas encore? On crée.
            o.close()
        except FileExistsError:# Erreur: ce fichier existe.
            o = open(file, mode='w')#On l'a déjà ? On écrase.
            o.close()
        savefig(fname=file, \
                format='png', \
                transparent=True, \
                frameon=False )# On enrengistre le fichier PNG 
        #avec un arrière-plan transparent.
        pause(0.005)# Temps d'arrêt entre les images.
    stdout.write("\n")
    close(fig)# Fermer la fenêtre du graphe.
    print("Terminé.")
graph()# On lance tout ça !