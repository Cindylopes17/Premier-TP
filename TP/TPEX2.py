#Distributeur de snack

sandwich_au_poulet:float = 4.90
Chips_Paprika:float = 2.50
Barre_Chocolat:float = 2.00
Bonbon:float = 3.30
Ice_Tea:float = 2.20
Limonade:float = 1.90

print("1. Sandwich au poulet")
print("2. Chips paprika")
print("3. Barre chocolat")
print("4. Bonbons")
print("5. Ice Tea")
print("6. limonade")

montant = float(input("Veuillez introduire votre monnaie :"))
selection = int(input("Veuillez sélectionner un produit :"))


if selection == 1 and montant >= sandwich_au_poulet:
    if montant != sandwich_au_poulet:
        print("Monnaie à rendre : " + str(round(montant-sandwich_au_poulet,2)))
    print("Sandwich au poulet ! Bon appetit !")
elif selection == 2 and montant >= Chips_Paprika:
    if montant != Chips_Paprika:
        print("Monnaie à rendre : " + str(round(montant-Chips_Paprika,2)))
    print("Chips Paprika ! Bon appetit !")
elif selection == 3 and montant >= Barre_Chocolat:
    if montant != Barre_Chocolat:
        print("Monnaie à rendre : " + str(round(montant-Barre_Chocolat,2)))
    print("Barre Chocolat servi ! Bon appetit !")
elif selection == 4 and montant >= Bonbon:
    if montant != Bonbon:
        print("Monnaie à rendre : " + str(round(montant-Bonbon,2)))
    print("Bonbon servi ! Bon appetit !")
elif selection == 5 and montant >= Ice_Tea:
    if montant != Ice_Tea:
        print("Monnaie à rendre : " + str(round(montant-Ice_Tea,2)))
    print("Ice tea servi ! Santé !")
elif selection == 6 and montant >= Limonade:
    if montant != Limonade:
        print("Monnaie à rendre : " + str(round(montant-Limonade,2)))
    print("Limonade servie ! Santé !")
else:
    print("Produit inconnu ou monnaie insuffisante")










montant = float(input("Veuillez introduire votre monnaie :"))
selection = int(input("Veuillez sélectionner un produit :"))