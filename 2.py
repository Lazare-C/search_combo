fichier = open("db/db.txt", "r")

lignes = fichier.read().splitlines()
fichier.close()


search = "xweezy7x@hotmail.com"


def recherche(search):
    for ligne in lignes:
        mail = ligne.split(":")
        if search in mail[0]:
            print(" \033[92m FIND: " + ligne)
            break
        else:
            print("\033[91m FAILD: " + ligne)
            # print(mail in ligne)



recherche(search)
