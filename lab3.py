import math


class Punkt:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    @staticmethod
    def distance(a, b):
        return math.sqrt((a.x - b.x) ** 2 + (a.y - b.y) ** 2)


class Adres:
    def __init__(self, nr_domu, ulica, miasto, kod_pocztowy, nr_mieszkania=None):
        self.nr_domu = nr_domu
        self.ulica = ulica
        self.miasto = miasto
        self.kod_pocztowy = kod_pocztowy

        if nr_mieszkania is not None:
            self.nr_mieszkania = nr_mieszkania

    def show(self) -> None:
        if hasattr(self, 'nr_mieszkania'):
            print(f'{self.ulica} {self.nr_domu}/{self.nr_mieszkania}')
            print(f'{self.kod_pocztowy} {self.miasto}')
            return None
        print(f'{self.ulica} {self.nr_domu}')
        print(f'{self.kod_pocztowy} {self.miasto}')

    def comes_before(self, other):
        for i in range(len(self.kod_pocztowy)):
            if self.kod_pocztowy[i] == other.kod_pocztowy[i]:
                continue
            if self.kod_pocztowy[i] < other.kod_pocztowy[i]:
                return True
            return False


class SodaCan:
    def __init(self, h, r):
        self.h = h
        self.r = r

    def get_volume(self) -> float:
        return math.pi * self.r * self.r * self.h

    def get_surface(self) -> float:
        return 2 * math.pi * self.r * (self.r * self.h)


class Car:
    def __init__(self, efficiency: float, max_fuel: float):
        self.efficiency = efficiency
        self.max_fuel = max_fuel
        self.current_fuel = 0

    def drive(self, distance: float) -> None:
        fuel_to_burn = distance / self.efficiency
        if fuel_to_burn > self.current_fuel:
            print('Nie ma tyle paliwa w baku lol.')
            return None
        self.current_fuel -= distance / self.efficiency

    def get_fuel_level(self) -> float:
        return self.current_fuel

    def add_fuel(self, fuel_amount: float) -> None:
        if fuel_amount + self.current_fuel > self.max_fuel:
            print('Nie ma tyle miejsca lol.')
            return None
        self.current_fuel += fuel_amount


class Student:
    def __init__(self, imie: str, nazwisko: str, *args):
        self.imie = imie
        self.nazwisko = nazwisko
        self.liczba_quizuw = len(args)
        try:
            suma = 0
            for i in args:
                suma += i
            self.srednia_quizuw = suma / self.liczba_quizuw
        except ZeroDivisionError:
            self.srednia_quizuw = 0


    def add_quiz(self, score):
        self.srednia_quizuw = ((self.srednia_quizuw * self.liczba_quizuw) + score) / (self.liczba_quizuw + 1)
        self.liczba_quizuw += 1

    def get_total_score(self):
        return self.srednia_quizuw * self.liczba_quizuw

    def get_average_score(self):
        return self.srednia_quizuw
