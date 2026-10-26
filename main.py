# Citire sir
sir = input("Introdu numere separate prin spatiu: ").split()
sir_numere = [int(x) for x in sir]
print(f"\nSirul citit este: {sir_numere}")

# Citire matrice
randuri = int(input("\nIntrodu numarul de randuri ale matricei: "))
coloane = int(input("Introdu numarul de coloane ale matricei: "))
matrice = []

print(f"Introdu elementele ({coloane} pe rand, separate prin spatiu):")
for i in range(randuri):
    rand_curent = input(f"Randul {i+1}: ").split()
    matrice.append([int(x) for x in rand_curent])

print("\nMatricea citita este:")
for rand in matrice:
    print(rand)


    # Citire din fisier
nume_fisier = input("\nIntrodu numele fisierului text (ex: date.txt): ")
try:
    with open(nume_fisier, "r") as f:
        continut = f.read().split()
        numere_fisier = [int(x) for x in continut]
        print(f"Valorile din fisier sunt: {numere_fisier}")
except FileNotFoundError:
    print(f"Eroare: Fisierul '{nume_fisier}' nu exista.")