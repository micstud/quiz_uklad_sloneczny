import json
import random


class Gracz:
    def __init__(self, name):
        self.name = name

    points = 0

    def quiz_l(self, pytania):
        for i in range(0,5):
            print(f"\nPytanie nr {i+1}")
            q = random.choice(pytania)
            pytania.remove(q)
            for key, value in q.items():
                if key.startswith("pytanie"):
                    print(value)
                if key != "poprawna" and key.startswith("pytanie") == False:
                    print(f"{key}. {value}")
            odp = input("Twoja odpowiedź: ")

            while odp != "a" and odp != "b" and odp != "c":
                odp = input("Wprowadź odpowiedź a, b, lub c: ")

            if odp == q["poprawna"]:
                print("Poprawna odpowiedź!")
                self.points += 1
            else:
                print("Niepoprawna odpowiedź!")
    
#funkcja nieużywana, wersja dla 1 gracza
    def quiz(self, pytania):
        for q in pytania:
            for key, value in q.items():
                if key != "poprawna":
                    print(f"{key}. {value}")
            odp = input("Twoja odpowiedź: ")
            if odp == q["poprawna"]:
                print("Poprawna odpowiedź!\n")
                self.points += 1
            else:
                print("Niepoprawna odpowiedź!\n")
        
        return self.points

def sortowanie(wyniki):
    sor_wyniki = {}
    lista = []
    for v in wyniki.values():
        print(v)
        lista.append(v)
    lista.sort(reverse=True)
    print(lista)
    while len(lista) > 0:
        w = lista.pop(0)
        for k,v in wyniki.items():
            if wyniki[k] == w:
                sor_wyniki[k] = v
    return sor_wyniki
    

if __name__ == "__main__":
    print("Quiz o Układzie Słonecznym\n")

    gracz1 = None
    gracz2 = None
    gracz3 = None
    gracz4 = None
    gracz5 = None

    gracze = [gracz1, gracz2, gracz3, gracz4,  gracz5]
    aktywni_gracze = []
    wyniki = dict()

    l = input("Wprowadź liczbę graczy (max.5): ")

    while l.isdigit() == False or int(l)>5 or int(l) < 1:
        l = (input("Wprowadź prawidłową wartość! "))

    l = int(l)

    nazwy_graczy = []
    for i in range(0,l):
        n_spr = input(f"Wprowadź nazwę {i+1} gracza: ")
        while n_spr in nazwy_graczy:
            n_spr = input(f"Nazwy graczy nie mogą się powtarzać! Wprowadź ponownie: ")
        gracze[i] = Gracz(n_spr)
        nazwy_graczy.append(n_spr)
        aktywni_gracze.append(gracze[i])

    with open("pytania-us.json") as questions:
        pytania1 = json.load(questions)

    for gracz in aktywni_gracze:
        print()
        print(f"{gracz.name} - wciśnij ENTER aby zacząć grę.")
        input()
        print(gracz.name)
        gracz.quiz_l(pytania1)

    

winner = None
best_score = None

score = dict()

for gracz in aktywni_gracze:
    score[gracz.name] = gracz.points

wyniki = sortowanie(score)
    
print("Ranking wyników: ")
m = 0
ps = None
for n, p in wyniki.items():
    if p != ps:
        m += 1
    print(f"{m}. {n}: {p}", end = "   ")
    if m == 1:
        print("ZWYCIĘZCA!")
    else:
        print()
    ps = p



