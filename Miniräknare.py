
# 1 Gör ett program som frågar användaren efter 3 tal. Sedan ska det räkna ut vad summan blir, och skriva ut på konsolen. (summa: tal1 + tal2 + tal3)
#
# 2 Programmet ska tala om vilket som är det största talet, utan att använda Python-funktionen max. Använd i stället if/elif/else. Fundera på om man kan lösa uppgiften på olika sätt.
#
# 3 Programmet ska tala om ifall två av talen är lika, eller alla tre är lika.
#
# 4 Programmet ska tala om vilket som är det mellersta talet. Observera att det bara finns ett mellersta tal om alla tre är olika, eller alla tre är lika. (Om talen skulle vara till exempel 2, 2, 5 så räknas inget av dem som mellerst i den här uppgiften.)
#
# För att testa systematiskt kan du göra en tabell. Kör sedan programmet. Kontrollera att programmet skriver ut samma saker som du har skrivit in i tabellen. Vi kallar talen t1, t2 och t3.
# Förslag på värden att testa med:  1 2 3, 1 3 2, 3 2 1, -1 -3 -1, 9 9 9, 32 32 16

tal1 = 0
tal2 = 0
tal3 = 0

t1 = int(input("Ange tal1: "))
t2 = int(input("Ange tal2: "))
t3 = int(input("Ange tal3: "))
summa = t1 + t2 + t3
print("summa av de tre talen är:",summa)

# case tal3 är störst
if t1 < t2 and t2 < t3:
    print("tal 3 är störst")
    print("det mellersta talet är tal 2")
# case tal2 störst
if t1 < t2 and t2 > t3:
    print("tal 2 är störst")
    print("det mellersta talet är tal 3")
# case tal1 störst
if t1 > t2 and t2 > t3:
    print("tal 1 är störst")
    print("det mellersta talet är tal 2")
# case  två eller alla tal lika
if t1 == t2 and t2 == t3:
    print("Alla tre talen är lika")
elif t1 == t2 or t2 == t3:
    print("två av talen är lika")