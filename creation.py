import pickle
mes_listes = []
class compte :
    def __init__(self) :
        self.name = ""
        self.prenom = ""
        self.age = 18
        self.taille = 175
        self.poids = 70
        self.mot_de_passe = ""
        self.mon_dico = {}
        self.ma_liste = []

    def saisir_save_user (self):
        self.name = input("Saisir votre nom : ")
        self.prenom = input("Saisir votre prenom : ")
        self.age = int(input("Saisir votre age : "))
        self.taille = float(input("Saisir votre taille en centimètre : "))
        self.poids = float(input("Entrez votre poids en kilogramme : "))
        self.mot_de_passe = input("Entrez votre mot de passe de 8 caractères : ")
        if len(self.mot_de_passe) != 8 :
            print("Ce mot de passe ne fait pas 8 caractères ")
            self.mot_de_passe = input("Entrez votre mot de passe de 8 caractères")
        self.mon_dico["nom"] = self.name
        self.mon_dico["prenom"] = self.prenom
        self.mon_dico["age"] = self.age
        self.mon_dico["taille"] = self.taille
        self.mon_dico["poids"] = self.poids
        self.ma_liste.insert(0,self.mon_dico)
        self.ma_liste.insert(1,self.mot_de_passe)
        mes_listes.append(self.ma_liste)
        with open("data.hm","ab") as file :
            pickle.dump (mes_listes,file)
    