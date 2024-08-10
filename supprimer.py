import pickle
from creation import compte
from login import connexion
from ouverture import ouvrir_liste
from verifier import verifier

def supprimer () :
    name = input("Entrer le nom du compte à supprimer : ")
    surname = input("Entrer le prenom du compte à supprimer : ")
    code = input("Entrer le mot de passe du compte à supprimer : ")
    mes_listes = ouvrir_liste()
    ma_liste = verifier (code,name,surname,mes_listes)
    if ma_liste is None :
        print("Suppression impossible ")
    else :
        listes = mes_listes.remove(ma_liste)
        print("Suppression effectuée")
        with open("data.hm","wb") as file :
            pickle.dump (mes_listes,file)
        print("bien")