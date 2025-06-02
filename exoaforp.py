import re

def verifier_mot_de_passe(mot_de_passe):
    longueur = len(mot_de_passe)
    majuscule = bool(re.search(r'[A-Z]', mot_de_passe))
    minuscule = bool(re.search(r'[a-z]', mot_de_passe))
    chiffre    = bool(re.search(r'\d', mot_de_passe))
    special    = bool(re.search(r'[^A-Za-z0-9]', mot_de_passe))

    types = majuscule + minuscule + chiffre + special

    # On exige à la fois longueur >= 12 ET au moins 3 types de caractères
    if longueur >= 12 and types >= 3:
        return True, []

    # Sinon, on recense ce qui manque
    manques = []
    if longueur < 12:
        manques.append("au moins 12 caractères")
    if not majuscule:
        manques.append("une majuscule")
    if not minuscule:
        manques.append("une minuscule")
    if not chiffre:
        manques.append("un chiffre")
    if not special:
        manques.append("un caractère spécial")
    if types < 3:
        manques.append("au moins 3 types de caractères différents "
                       "(majuscules, minuscules, chiffres, caractères spéciaux)")
    return False, manques


if __name__ == "__main__":
    essais = 3
    for tentative in range(essais):
        mdp = input("Saisissez votre mot de passe : ")
        conforme, manques = verifier_mot_de_passe(mdp)

        if conforme:
            print("Mot de passe conforme aux recommandations de l'ACNIL.")
            break
        else:
            print("Mot de passe non conforme aux recommandations de l'ACNIL.")
            # On affiche la liste des éléments manquants (sans doublons)
            print("Il manque : " + ", ".join(set(manques)))

            # Récapitulatif détaillé après chaque tentative infructueuse
            longueur = len(mdp)
            types_detectes = sum(bool(x) for x in [
                re.search(r'[A-Z]', mdp),
                re.search(r'[a-z]', mdp),
                re.search(r'\d', mdp),
                re.search(r'[^A-Za-z0-9]', mdp)
            ])
            print(f"→ Longueur saisie : {longueur} caractère(s).")
            print(f"→ Types de caractères présents : {types_detectes}.")

            if longueur < 12:
                print(f"  Il manque {12 - longueur} caractère(s) pour atteindre 12.")
            if types_detectes < 3:
                print(f"  Il manque {3 - types_detectes} type(s) de caractères "
                      "pour atteindre 3.")

            # Nombre d'essais restants
            restantes = essais - tentative - 1
            if restantes > 0:
                print(f"Il vous reste {restantes} essai(s).\n")
            else:
                print()  # simple saut de ligne avant le message d'échec final

    else:
        # Cette partie ne s'exécute que si on n'a jamais fait de `break`
        print("Nombre d'essais dépassé. Veuillez réessayer plus tard.")
