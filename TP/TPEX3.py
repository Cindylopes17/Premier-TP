#Risque Cardiovasculaire


age: int = int(input("Quel est votre age?"))
sexe: str = input("Quel est votre sexe ? (h ou f)")
fumeur:str = input("Etes-vous fumeur? (oui ou non)")
sport : str = input("Faites-vous du sport (oui ou non)")

niveau_risque: int = 0

if fumeur == "oui":
        niveau_risque +=2
if sport == "oui":
        niveau_risque -=1
if age > 50 and sexe == "h":
    niveau_risque +=1
if age > 60 and sexe == "f":
    niveau_risque +=1


if niveau_risque <= 1:
    print("niveau de risque faible")
else:
    print("niveau de risque élevé")
