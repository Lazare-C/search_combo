import os

def search_db(mail):
    result  = []
    question = variable.get()
    recherche = question.split()
    mots = open('tsuDB.txt', 'r')      #choisier la db ou trouver le mdp

    for resultat in recherche:
        for entree in mots:
            if resultat in entree:
                result.append(resultat)
                try:
                    fen.retour
                except:
                    print 'la variable n\'existe pas'
                else:
                    fen.retour.destroy()

    final = ' '.join(result)
    fen.retour = Label(fen,text=final ,foreground="red",width=100)
    fen.retour.pack()

fen.boutton = Button(fen,text="valider",command=reponse)

variable.pack()
fen.boutton.pack()
fen.mainloop()
