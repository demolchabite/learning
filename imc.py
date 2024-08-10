from creation import compte
from login import connexion
from ouverture import ouvrir_liste
from verifier import verifier
def calcul (user) :
    imc = user.poids / (user.taille *10**(-2) )**2
    return imc

def conseil (imc) :
    if imc < 18.5:
        return "Underweight: You may need to gain weight for your health."
    elif 18.5 <= imc < 24.9:
        return "Normal weight: You are in a healthy weight range."
    elif 25 <= imc < 29.9:
        return "Overweight: You may need to lose weight for your health."
    elif 30 <= imc < 34.9:
        return "Obesity Class 1: Increased risk of health problems. Consider losing weight."
    elif 35 <= imc < 39.9:
        return "Obesity Class 2: High risk of health problems. Strongly consider losing weight."
    else:
        return "Obesity Class 3: Very high risk of severe health problems. Medical intervention may be needed."

    