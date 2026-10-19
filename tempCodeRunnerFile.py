print("--- Cerința 2 ---")
nume_fisier = input("Fișierul de citit?")

try:
    fisier = open(nume_fisier, "r")
    text_fisier = fisier.read()
    print("Nr din fișier sunt:", text_fisier.split())
except:
    print("Unde e fișierul fra?")