# För att få åka Balder på Liseberg måste man vara 130 cm lång.
# Skriv ett program som kan säga om man får åka!

# svar diskutera. Varför man måste testa just tre värden...
# Beror på hur programet är utformat, tex om man använder satsen
# "if length <= 130:", så svarar det fel om man skriver in 130 eftersom <= ger True på (mindre och lika med)

length = int(input("Skriv in din längd i cm: "))

if length < 130:
    print("Du kan inte åka ")
elif length >= 130:
    print("Du kan åka ")


