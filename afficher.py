import pickle
from creation import compte
from login import connexion
from ouverture import ouvrir_liste
from verifier import verifier

def afficher ():
    mes_listes = ouvrir_liste()
    for innerlist in mes_listes :
        print(innerlist)