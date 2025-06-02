# TP Thème 1 – "CrackMe" : Jeu de mots de passe faibles

import random

# 1. Liste des mots de passe faibles
mots_de_passe_faibles = [
    "123456", "password", "admin", "123456789", "qwerty",
    "abc123", "letmein", "welcome", "monkey", "football"
]

# Bonus : possibilité de charger depuis un fichier texte
def charger_mots_de_passe(fichier):
    try:
        with open(fichier, "r") as f:
            return [ligne.strip() for ligne in f if ligne.strip()]
    except FileNotFoundError:
        return mots_de_passe_faibles

# Demander si on veut charger depuis un fichier
utiliser_fichier = input("Charger les mots de passe depuis un fichier ? (o/n) : ").lower() == "o"
if utiliser_fichier:
    chemin = input("Nom du fichier (ex: mots.txt) : ")
    mots_de_passe = charger_mots_de_passe(chemin)
else:
    mots_de_passe = mots_de_passe_faibles

# 2. Sélection aléatoire
mot_secret = random.choice(mots_de_passe)

# Bonus : Limite d'essais
max_essais = int(input("Nombre maximum d'essais autorisés ? (0 = illimité) : "))
essais = 0
historique = []

print("Tapez 'triche' pour révéler le mot de passe (pour tester).")

while True:
    tentative = input("Devinez le mot de passe : ")
    if tentative == "triche":
        print(f"[TRICHE] Le mot de passe est : {mot_secret}")
        continue
    essais += 1
    historique.append(tentative)
    if tentative == mot_secret:
        print(f"Bravo ! Mot de passe trouvé en {essais} essais.")
        break
    # 4. Indices
    indice = []
    if len(tentative) < len(mot_secret):
        indice.append("Le mot de passe est plus long.")
    elif len(tentative) > len(mot_secret):
        indice.append("Le mot de passe est plus court.")
    if tentative and tentative[0] == mot_secret[0]:
        indice.append("Il commence par la même lettre.")
    lettres_communes = len(set(tentative) & set(mot_secret))
    indice.append(f"{lettres_communes} lettre(s) en commun.")
    print("Indice :", " | ".join(indice))
    # Bonus : Limite d'essais
    if max_essais and essais >= max_essais:
        print(f"Nombre maximum d'essais atteint. Le mot de passe était : {mot_secret}")
        break

# Bonus : Afficher l'historique
print("Historique des tentatives :", historique)