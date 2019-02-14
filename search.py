# coding: utf-8
import glob
import errno
import sys
path = 'db/*.txt'
files = glob.glob(path)

for name in files:
    try:
        with open(name) as f:
            fichier = open(name, "r")

            lignes = fichier.read().splitlines()
            fichier.close()

            search = "agateargent@gmail.com"

            def recherche(search):
                i = 0
                for ligne in lignes:
                    mail = ligne.split(":")
                    if search in mail[0]:
                        print(" \033[92m FIND: " + ligne + "\n Trouve dans: " + name)
                        print("nombre de temtative: " + str(i))
                        exit(0)
                        break
                    else:
                        print("\033[91m FAILD: " + ligne)
                        i += 1
                print("nombre de temtative: " + str(i))

            recherche(search)

    except IOError as exc:
        if exc.errno != errno.EISDIR:
            raise
