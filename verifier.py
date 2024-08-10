import pickle
from login import connexion
from ouverture import ouvrir_liste
from creation import compte


def verifier (code,name,surname,mes_listes) : 
    for innerlist in mes_listes :
        result = connexion(code,name,surname,innerlist)
    if result is None :
        print("Votre compte n'existe pas ")
    else :
        print("Vous avez été identifé ")
        return result
        
