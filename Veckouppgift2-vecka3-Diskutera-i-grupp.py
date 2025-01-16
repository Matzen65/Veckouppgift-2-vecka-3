#
'''
 Diskutera i grupp
 1. Syftet med koden är att beräkna en rabatt beroende på vilka belopp man handlat för
 2.
 3. Programmet krachar då man försökt addera ett float till en sträng i utskriften. (byt + mot ,)
 4. logiska fel är ...
        * programet kör bägge beräkningsfallen och adderar 35% discount pga att bägge IF-satserna beräknas.
        Avhjälps med en "elif" i den andra IF-satsen.
        * Ett fel till är att programmet inte fått info huruvida användaren är medlem
5. se ovan förklaringar i punkt 3 och 4
6. Koden har förbättrats med ovanstående punkter samt en fråga om man är medlem eller ej.
    I övrigt kan man lägga in en fråga om namn om man inte är medlem
'''

namn = "Du är medlem, "
is_member = False
level1 =100
level2 = 300
discount = 0

member = input("Är du medlem? ange med ja eller nej: ")
if member == "ja":
    is_member = True

if member != "ja":
    namn = input("Vill du bli medlem så ange in ditt namn, annars tryck enter för att gå vidare ")
    if namn == "":
        is_member = False
        print("du är ej medlem, tryck enter för att handla vidare: ")

price = input(f"Välkommen: {namn} köp något dyrt och ange pris: ")

price = float(price)
if price >= level1 and price <= level2:
    print("Grattis! Du har avancerat till nivå 1 och får 10% rabatt.")
    discount = discount + 10
elif price >= level2:
    print("Grattis! Du har avancerat till nivå 2 och får 25% rabatt.")
    discount = discount + 25

final_price = price - (price * discount / 100)
print("Efter rabatter blir priset.... ", final_price)