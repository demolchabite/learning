from creation import compte
from login import connexion
from ouverture import ouvrir_liste
from verifier import verifier
from supprimer import supprimer
from afficher import afficher
def main ():
    user = compte()
    user.saisir_save_user()
    """code = input("Entrez votre mot de passe : ")
    name = input("Entrez votre nom : ")
    surname = input("Entrer votre prenom : ")
    mes_listes = ouvrir_liste() 
    verifier (code,name,surname,mes_listes)"""
    #supprimer ()
    afficher()

if __name__ == "__main__":
    main()