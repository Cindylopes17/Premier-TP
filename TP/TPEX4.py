#Compagnie d'assurance

age: int = int(input("Quel age avez-vous?"))
permis: int = int(input("Nombre d'années de permis?"))
accidents: int = int(input("Nombre d'accidents ?"))
annéesAssurance: int = int(input("Nombre d'années d'assurance ?"))

Vert: str = "vert"
Bleu: str = "bleu"
Rouge: str = "rouge"
Orange: str = "orange"

couleur: str = None

if age < 25 and permis < 2 and accidents == 0:
     couleur = Rouge
elif (age < 25 and permis > 2 and accidents == 0) or (age > 25 and permis < 2 and accidents == 0):
    couleur = Orange
    if accidents == 1:
        couleur = Rouge
elif age > 25 and permis > 2 and accidents <= 1:
    if accidents == 1:
        couleur = Orange
    else:
        couleur = Vert
else: #accidents == 2:
    print("Refusé")
#if annéesAssurance > 5:
    #vert devient bleu
    #Orange devient vert
    #Rouge devient orange
if annéesAssurance > 5:
    if couleur == Orange:
        couleur = Vert
    elif couleur == Rouge:
        couleur = Orange
    elif couleur == Vert:
        couleur = Bleu
print(couleur)



