#1.
#A)

print(type(1 + 2)) #int - operator "+" sumuje dwie liczby całkowite
print(type(1 + 4.5)) #float - operator "+" sumuje liczbę całkowitą i zmiennoprzecinkową
print(type(3 / 2)) #float - operator "/" dzieli dwie liczby całkowie
print(type(4 / 2)) #float - operator "" dzieli dwie liczby całkowie
print(type(3 // 2)) #int - operator "//" wykonuje dzielenie całkowite, zwracając całkowitą część wyniku
print(type(-3 // 2)) #int - operator "//" wykonuje dzielenie całkowite, wynik zaokrąglony w dół)
print(type(11 % 2)) #int - operator "%" zwraca resztę z dzielenia dwóch liczb
print(type(2 ** 10)) #int - operator "**" wykonuje potęgowanie
print(type(8 **(1/3))) #float - operator "**" wykonuje potęgowanie

#B)

print(int(3.0)) #konwertowanie liczby zmiennoprzecinkowej float do liczby całkowitej int
print(float(3)) #konwertowanie libczy całkowitej int na do liczby zmiennoprzecinkowej float
print(float("3")) #konwertowanie napisu string, który zawiera lcizbę "3" do liczby zmiennoprzecinkowej float
print(str(12.4)) #konwertowanie na zapis bez nawiasów
print(bool(0)) #sprawdzanie czy jest zachowana wartość logiczna. Jest "0" dlatego false.

#2.
uczelnia = "Studiuję na WSIiZ"
print(uczelnia)

#3.
imię = "Jan"
wiek = "20"
wzrost = "178"

print(f"Nazywam się {imię} i mam {wiek} lat.")
print(f"Mój wzrost to {wzrost} cm")

#4.
Cena = 39.99
Rabat = 0.2
Cena_produktu = Cena * (1 - Rabat)
print(f"Cena_produktu: {Cena_produktu:.2f} PLN")

#5.
dlugosc = float(input("Podaj długość prostokąta: "))
szerokosc = float(input("Podaj szerokosc prostokąta: "))

pole = dlugosc * szerokosc
obwod = 2 * (dlugosc + szerokosc)

print(f"Pole prostokąta: {pole:.2f}")
print(f"Obwód prostokąta: {obwod:.2f}")

#6.
droga = float(input("Podaj ilość kilometrów: "))
spalanie = float(input("Podaj średnie spalanie w litrach na 100km: "))
cena_paliwa = 6.5
przewidywane_zuzycie_paliwa = (droga * spalanie) / 100
koszt_podrozy = przewidywane_zuzycie_paliwa * cena_paliwa

print(f"Przewidywane zużycie paliwa: {przewidywane_zuzycie_paliwa:.2f} litrów")
print(f"Szacowany koszt podróży: {koszt_podrozy:.2f} złotych")

#A)
import random
droga = random.randint(50, 500)
print(f"Wylosowana długość przejechanej drogi: {droga} km")

spalanie = float(input("Podaj średnie spalanie w litrach na 100km: "))
cena_paliwa = float(input("Podaj aktualną cenę paliwa w zł na litr: "))

zuzycie_paliwa = (droga * spalanie) / 100
koszt_podrozy = zuzycie_paliwa * cena_paliwa

print(f"Przewidywane zużycie paliwa: {zuzycie_paliwa:.2f} litrów")
print(f"Szacowany koszt podrózy: {koszt_podrozy:.2f}")

#B)
droga = random.randint(50, 500)
print(f"Wylosowana długość przejechanej drogi: {droga} km")

spalanie = float(input("Podaj średnie spalanie (l/100 km): "))
cena_paliwa = float(input("Podaj aktualną cenę paliwa (zł/l): "))

zuzycie_paliwa = (droga * spalanie) / 100
koszt_podrozy = zuzycie_paliwa * cena_paliwa

print(f"Długość drogi: {droga} km")
print(f"Średnie spalanie: {spalanie:.2f} l/100 km")
print(f"Przewidywane zużycie paliwa: {zuzycie_paliwa:.2f} l")
print(f"Szacowany koszt podróży: {koszt_podrozy:.2f} zł")

#7.
a = float(input("Podaj współczynnik a: "))
b = float(input("Podaj współczynnik b: "))

if a == 0:
    if b == 0:
        print("Równanie ma nieskończenie wiele rozwiązań.")
    else:
        print("Równanie jest sprzeczne i nie ma rozwiązań.")
else:
    x = -b / a
    print(f"Rozwiązanie równania to: x = {x:.2f}")


#8.
import math

a = float(input("Podaj współczynnik a: "))
b = float(input("Podaj współczynnik b: "))
c = float(input("Podaj współczynnik c: "))

if a == 0:
    if b == 0:
        if c == 0:
            print("Równanie ma nieskończenie wiele rozwiązań.")
        else:
            print("Równanie jest sprzeczne i nie ma rozwiązań.")
    else:
        x = -c / b
        print(f"Równanie jest liniowe, rozwiązanie to: x = {x:.2f}")
else:
    delta = b**2 - 4 * a * c

    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        print(f"Równanie ma dwa pierwiastki: x1 = {x1:.2f}, x2 = {x2:.2f}")
    elif delta == 0:
        x = -b / (2 * a)
        print(f"Równanie ma jeden pierwiastek: x = {x:.2f}")
    else:
        print("Równanie nie ma rozwiązań rzeczywistych.")

#9.

liczba1 = float(input("Podaj pierwszą liczbę: "))
liczba2 = float(input("Podaj drugą liczbę: "))

dodawanie = liczba1 + liczba2
odejmowanie = liczba1 - liczba2
mnozenie = liczba1 * liczba2
dzielenie = liczba1 / liczba2
potegowanie = liczba1 ** liczba2

# Wyświetlanie wyników za pomocą f-string
print(f"Wynik dodawania: {dodawanie}")
print(f"Wynik odejmowania: {odejmowanie}")
print(f"Wynik mnożenia: {mnozenie}")
print(f"Wynik dzielenia: {dzielenie}")
print(f"Wynik potęgowania: {potegowanie}")








