import sys
from typing import Any, Callable


class ListaWpis:
    def __init__(self, wart: str = '', poprz: 'ListaWpis' = None, nast: 'ListaWpis' = None):
        self.wart = wart
        self.poprz = poprz
        self.nast = nast

    def dodaj_po_nim(self, wart: Any) -> None:
        node = ListaWpis(wart)
        node.poprz = self
        node.nast = self.nast
        self.nast.poprz = node
        self.nast = node

    def dodaj_przed_nim(self, wart: Any) -> None:
        node = ListaWpis(wart)
        node.poprz = self.poprz
        node.nast = self
        self.poprz.nast = node
        self.poprz = node


class Lista2k2w:
    def __init__(self):
        self.przed_pie = ListaWpis('przed_pie')
        self.za_ost = ListaWpis('za_ost')

        self.przed_pie.nast = self.za_ost
        self.za_ost.poprz = self.przed_pie

    def podaj_dlugosc(self) -> int:
        counter = 0
        pointer = self.przed_pie.nast

        while pointer != self.za_ost:
            counter += 1
            pointer = pointer.nast

        return counter

    def pobierz_el(self, id: int) -> ListaWpis:
        if self.przed_pie.nast is self.za_ost:
            sys.exit('You are trying to get element from empty list...')

        if id < 0:
            return self.__pobierz_el_tyl(-id - 1)
        return self.__pobierz_el_przud(id)

    def __pobierz_el_przud(self, id: int) -> ListaWpis:
        pointer = self.przed_pie.nast
        counter = 0

        while True:
            while pointer != self.za_ost:
                if counter is id:
                    return pointer
                pointer = pointer.nast
                counter += 1

            pointer = self.przed_pie.nast

    def __pobierz_el_tyl(self, id: int) -> ListaWpis:
        pointer = self.za_ost.poprz
        counter = 0

        while True:
            while pointer != self.przed_pie:
                if counter is id:
                    return pointer
                pointer = pointer.poprz
                counter += 1

            pointer = self.za_ost.poprz

    def dodaj_za_koniec(self, wart: Any) -> None:
        node = ListaWpis(wart)
        node.poprz = self.za_ost.poprz
        self.za_ost.poprz.nast = node
        node.nast = self.za_ost
        self.za_ost.poprz = node

    def dodaj_na_poczatek(self, wart: Any) -> None:
        node = ListaWpis(wart)
        node.poprz = self.przed_pie
        node.nast = self.przed_pie.nast
        self.przed_pie.nast.poprz = node
        self.przed_pie.nast = node

    def __str__(self) -> str:
        if self.przed_pie.nast is self.za_ost:
            return 'List is empty'

        pointer = self.przed_pie.nast
        printText = ''

        while pointer != self.za_ost:
            printText += f'"{pointer.wart}"'

            if pointer != self.za_ost.poprz:
                printText += ' -> '

            pointer = pointer.nast

        return printText

    def print(self) -> None:
        print(self)

    def usun_pierwszy(self) -> str:
        if self.przed_pie.nast is self.za_ost:
            return 'Cannot remove, sorry'

        node = self.przed_pie.nast
        self.przed_pie.nast = node.nast
        node.poprz = self.przed_pie

        return node.wart

    def usun_ostatni(self) -> str:
        if self.przed_pie.nast is self.za_ost:
            return 'Cannot remove, sorry'

        node = self.za_ost.poprz
        self.za_ost.poprz = node.poprz
        node.poprz.nast = self.za_ost

        return node.wart

    def obrub_wartosci(self, fun: Callable[[str], str]) -> None:
        pointer = self.przed_pie.nast

        while pointer != self.za_ost:
            pointer.wart = fun(pointer.wart)
            pointer = pointer.nast

    def odwruc(self) -> 'Lista2k2w':
        pointer = self.za_ost.poprz
        lista = Lista2k2w()

        while pointer != self.przed_pie:
            lista.dodaj_za_koniec(pointer.wart)
            pointer = pointer.poprz

        return lista
