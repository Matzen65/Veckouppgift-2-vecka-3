#Tottenham spelar mot Liverpool i Champions League.
# Skriv ett program som frågar användaren hur många mål respektive lag gjorde,
# och talar om vilket lag som vann.

tottenham = 0
liverpool = 0
goaldiff = 0

print("Matchen är över, nu ska vi räkna ut resultatet! ")
tottenham = int(input("Hur många mål gjorde Tottenham?: "))
liverpool = int(input("Hur många mål gjorde Liverpool?: "))

if tottenham > liverpool:
    goaldiff = tottenham - liverpool
    print("Tottenham vann med ",goaldiff,"mål" )
elif tottenham < liverpool:
    goaldiff = liverpool - tottenham
    print("liverpool vann med ", goaldiff, "mål")
elif tottenham == liverpool:
    print("Det blev oavgjort! ")