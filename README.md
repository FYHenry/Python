# Python

Petits projets de développement en Python regroupés dans des répertoires partageant un environnement virtuel similaire.

Pour installer chaque répertoire `DIR`:
```bash
cd $DIR
python -m venv ./
pip3 install -r requirements.txt
```

Pour exécuter les programes:
```sh
#Shell POSIX
source ./bin/activate
```

Pour quitter l’environement:
```sh
#Shell POSIX
deactivate
```

Dans le cas de `MatPlotLib/` une installation des paquets DEB `libgirepository1.0-dev`, `gcc`,
 `libcairo2-dev`, `pkg-config`, `python3-dev` et `gir1.2-gtk-3.0` peut être nécessaire¹.
La commande `pip3` vient après.
Ainsi *MatPlotLib* peut afficher ses graphes via *GTK+3*.

1 [PyGObject Doc.](https://pygobject.readthedocs.io/en/latest/getting_started.html)
