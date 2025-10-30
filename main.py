import random

def losowanie_liczb(liczbaKostek):
    listaWynikow = []
    for i in range(liczbaKostek):
        print(f"Kostka {i + 1}: ", random.randint(1, 6))

def liczenie_punktow():


if __name__ == "__main__":
    liczbaKostek = int(input("Podaj liczbę kostek do rzucenia (3 - 10): "))

    while liczbaKostek < 3 or liczbaKostek > 10:
        liczbaKostek = int(input("Podaj liczbę kostek do rzucenia (3 - 10): "))

    losowanie_liczb(liczbaKostek)