#!/usr/bin/env python
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

            if len(sys.argv) != 1:
                search = sys.argv[1]
            else:
                search = "mail@mail.fr" #if you do not use the arguments enter the mail here


            def recherche(search):
                i = 0
                for ligne in lignes:
                    mail = ligne.split(":")
                    if search in mail[0]:
                        print("\033[92mFIND: " + ligne + "\nFound in: " + name)
                        print("number of attempted: " + str(i))
                        exit(0)
                        break
                    else:
                        print("\033[91mFAILD: " + ligne)
                        i += 1
                print("\033[91m" + search + " was not found")
                print("number of attempted: " + str(i))

            recherche(search)

    except IOError as exc:
        if exc.errno != errno.EISDIR:
            raise
