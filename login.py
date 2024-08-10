from ouverture import ouvrir_liste
from creation import compte
def connexion (code,name,surname,ma_liste) : 
    verify = False
    if ma_liste[1] == code and ma_liste[0]["nom"] == name and ma_liste[0]["prenom"] == surname :
        """print("Vous avez bien été identifié ")
        verify = True
        print(verify)"""
        return ma_liste
