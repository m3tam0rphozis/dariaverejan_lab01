print("--- Cerința 1 ---")
text = input("Scrie numere cu spațiu între ele: ")
print("Șirul tău este:", text.split())

linii = int(input("Câte linii are matricea? "))
coloane = int(input("Câte coloane are matricea? "))
matrice = []
for i in range(linii):
    linie = input(f"Scrie numerele pentru linia {i+1}: ")
    matrice.append(linie.split())

print("Matricea ta este:")
print(matrice)