import pickle
def ouvrir_liste () :
    with open ("data.hm","rb") as f :
        mes_listes = pickle.load (f)
        return mes_listes