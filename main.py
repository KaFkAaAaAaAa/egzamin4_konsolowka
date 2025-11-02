import random

def losowanie_liczb(liczbaKostek):
    listaWynikow = []
    for i in range(liczbaKostek):
        wynik = random.randint(1, 6)
        listaWynikow.append(wynik)
        print(f"Kostka {i + 1}: ", wynik)
    return listaWynikow

def liczenie_punktow(listaWynikow):
    punkt = 0
    for i in range(1, 7):
        if listaWynikow.count(i) >= 2:
            punkt += i * listaWynikow.count(i)
    return punkt

if __name__ == "__main__":
    while True:
        liczbaKostek = int(input("Podaj liczbę kostek do rzucenia (3 - 10): "))

        while liczbaKostek < 3 or liczbaKostek > 10:
            liczbaKostek = int(input("Podaj liczbę kostek do rzucenia (3 - 10): "))

        listaWynikow = losowanie_liczb(liczbaKostek)
        punkt = liczenie_punktow(listaWynikow)
        print(f"Liczba uzyskanych punktów: {punkt}")

        ponowienie = input("Jeszcze raz (t/n)? ")
        if ponowienie != "t":
            break