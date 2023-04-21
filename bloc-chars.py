#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Spyder Editor

Bloc characters
"""

from sys import argv

def cadres():
  texte = "\tCaractères Cadres\n\r\n\r       "
  
  for c in range(0x00, 0x10, 0x01):
    texte += "{:x} ".format(c)
    if c == 0x0f:
      texte += "\n\r\n\r"
  
  for l in range(0x0, 0x8, 0x1):
    texte += "0x25{:x}. ".format(l)
    for c in range(0x00, 0x10, 0x01):
      texte += "{:c} ".format(0x2500 + 0x10*l + c)
      if c == 0x0f:
        texte += "\n\r"
  
  print(texte)
  
def blocs():
  texte = "\n\r\tCaractères Blocs\n\r\n\r       "
  
  for c in range(0x00, 0x10, 0x01):
    texte += "{:x} ".format(c)
    if c == 0x0f:
      texte += "\n\r\n\r"
  
  for l in [0x8, 0x9]:
    texte += "0x25{:x}. ".format(l)
    for c in range(0x00, 0x10, 0x01):
      texte += "{:c} ".format(0x2500 + 0x10*l + c)
      if c == 0x0f:
        texte += "\n\r"
  
  print(texte)

if len(argv) > 1 and (argv[1] == "-a" or argv[1] == "--all"):
  cadres()
  blocs()
  
elif len(argv) <= 1 or (argv[1] == "-h" or argv[1] == "--help"):
  print("""Usage :
        {a:s} -a|--all
        \tÉcrit tous les caractères
        {a:s} [-h|--help]
        \tÉcrit cette aide
        {a:s} (-c|--character) CHAR
        \tÉcrit le caractère CHAR
        """.format(a=argv[0]))
        
elif len(argv) > 2 and (argv[1] == "-c" or argv[1] == "--character"):
  nombre = int(argv[1], 16)
  if nombre <= 0x2500 and nombre > 0x2600:
    print(hex(nombre))
