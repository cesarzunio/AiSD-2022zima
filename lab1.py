def zad1(literaImienia : str, nazwisko : str):
    return f"{literaImienia} . {nazwisko}"


def zad2(imie : str, nazwisko : str):
    return (str(imie[0])).capitalize() + ". " + (str(nazwisko)).capitalize()


def zad3(dwiePierwsze, dwieOstatnie, wiek):
    rok = int(str(dwiePierwsze) + str(dwieOstatnie))
    return rok - int(wiek)


def zad4(imie, nazwisko, func):
    return func(imie, nazwisko)


def zad5(x, y):
    if x > 0 and y > 0: # and y != 0 ??
        return x / y
    return 0


def zad6():
    suma = 0
    while suma < 100:
        suma += float(input("Podaj liczbe: "))
        print(f"Aktualna suma: {suma}")


def zad7(list : []):
    return tuple(list)


def zad8():
    list = []
    while len(list) < 10:
        list.append(input("Podaj liczbe (albo cos innego): "))
    return tuple(list)



def zad9(i : int):
    tygodnie = ['Poniedzialek', 'Wtorek', 'Sroda', 'Czwartek', 'Pjontek', 'Sobota', 'Niedziela']
    return tygodnie[i - 1]


def zad10(tekst):
    length = len(tekst) - 1
    mid = int(length / 2)
    if length % 2 == 1:
        mid += 1
    for i in range(mid):
        # print(tekst[i])
        # print(tekst[length - i])
        if tekst[i] != tekst[length - i]:
            return False
    return True
