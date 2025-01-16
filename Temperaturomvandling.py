# Skriv ett program som kan omvandla en temperatur i
# grader Celsius till grader Fahrenheit.

celcius = float(0)
fahrenheit = float(0)

temp_slag = input("Ange om du vill ange temperaturen i C eller F: ")

if temp_slag == "C" or temp_slag == "c":
    celsius = float(input("Skriv in en temperatur i grader Celsius: "))
    fahrenheit = 1.8 * celsius + 32
    print("Det blir ", fahrenheit, "grader Fahrenheit.")

if temp_slag == "F" or temp_slag == "f":
    fahrenheit = float(input("Skriv in en temperatur i grader Fahrenheit: "))
    celsius = (fahrenheit - 32) / 1.8
    print("Det blir ", celsius, "grader Celcius.")

if celsius <= 10:
    print("Ta på dig vinterkläder")
if celsius >= 20:
    print("Packa badkläder")