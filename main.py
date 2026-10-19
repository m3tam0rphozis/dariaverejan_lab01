print("--- Cerința 1 ---")
text = input("Introdu niște nr (cu spațiu între ele): ")
print("Șirul tău este:", text.split())

linii = int(input("Linii?"))
coloane = int(input("Coloane?"))
matrice = []
for i in range(linii):
    linie = input(f"Nr pentru linia {i+1}: ")
    matrice.append(linie.split())

print("Matricea:")
print(matrice)


print("--- Cerința 2 ---")
nume_fisier = input("Fișierul de citit?")

try:
    fisier = open(nume_fisier, "r")
    text_fisier = fisier.read()
    print("Nr din fișier sunt:", text_fisier.split())
except:
    print("Unde e fișierul fra?")