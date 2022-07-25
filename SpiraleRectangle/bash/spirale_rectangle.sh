#!/usr/bin/env bash

# Ce petit fichier permet de créer un fichier image GIF à partir d'un séquençage de fichiers PNG. Suite 
#+à un script Python du nom de spirale_rectangle.py.
# La commande convert de ImageMagick permet de retaper cette suite d'images et leur séquençage.

# On est dans le répertoire-racine du projet : projet_spirale_rectangle/.
echo " " ;
echo "Troncage des images." ;
echo " " ;
for IMAGE_NO in $( seq 0 39 ; ) ; #Sur plusieurs fichiers PNG...
do
	convert -verbose -crop 126x94+327+149 +repage ./data/spirale$( printf "%03d" "$IMAGE_NO" ).png \
		./data/spiralebis$( printf "%03d" "$IMAGE_NO" ).png #On rogne bien chaque image.
done ;
for i in $( seq 0 39 ) ;
do
	IMAGE_LISTE[$i]=./data/spiralebis$( printf "%03d" "$i" ).png ; #Liste des nouveaux fichiers PNG.
done ;
echo " " ;
echo "Création du fichier GIF." ;
echo " " ;
LISTE=${IMAGE_LISTE[@]} ;
convert -verbose -dispose previous -delay 10 -loop 0 $LISTE ./output/spirale_rectangle.gif ; #Puis on assemble en un fichier GIF.
echo "Terminé." ;
