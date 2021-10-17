#Billet de cinéma
prix:int = 10
Rabais_étudiant:int = 2
Rabais_membre:int = 3
Fofait_famille:int = 1


Carte_mensuelle: str =input("Possédez-vous la carte mensuelle ? (oui ou non)")
#Carte_membre #: str = input("Possédez-vous la carte membre ? (oui ou non)")
#Carte_étudiant #: str = input("Possédez-vous la carte étudiante ? ( oui ou non)")
#Forfait_famille #: str = input("Possédez-vous le forfait famille? (oui ou non)")

if Carte_mensuelle == "non":
    Carte_étudiant:str = input("Possédez-vous la carte étudiante ? ( oui ou non)")
    Carte_membre:str = input("Possédez-vous la carte membre ? ( oui ou non )")
    Carte_famille:str = input("Possédez-vous le forfait famille ? (oui ou non)")
    if Carte_étudiant == "oui":
        prix -= Rabais_étudiant
    if Carte_membre == "oui":
        prix -= Rabais_membre
    if Carte_famille == "oui":
        prix -= Fofait_famille
    if Carte_étudiant == "oui" and Carte_membre == "oui":
        prix -= Rabais_étudiant + Rabais_membre
    if Carte_membre == "oui" and Carte_famille == "oui":
            prix -= Rabais_membre + Fofait_famille
    if Carte_famille == "oui" and Carte_étudiant == "oui":
        prix -= Rabais_étudiant
else:
    prix = "Entrée gratuite"
print("le prix a payer est : " + str(prix) + "CHF")


