import sys


def numbers(n: int) -> None:
    if n < 0:
        sys.exit('Check ur code bruh')
    if n == 0:
        print(0)
        return
    print(n)
    numbers(n - 1)


def factorial(n: int):
    if n < 0:
        sys.exit('Check ur code bruh')
    if n < 3:
        return n
    return n * factorial(n - 1)


def power(a: int, n: int) -> int:
    if n < 0:
        a = 1 / a
        n = -n
    elif n == 0:
        return 1
    return a * power(a, n - 1)


def prime(n: int) -> bool:
    if n < 0:
        sys.exit('Check ur code bruh')

    def prime_helper(n: int, p: int) -> bool:
        if n == p:
            return False
        return n % p == 0 or prime_helper(n, p + 1)

    return not prime_helper(n, 2)


def reverse(text: str) -> str:
    if len(text) < 2:
        return text

    def reverse_helper(text: str, n: int):
        if n == len(text):
            return text[-n]
        return text[-n] + reverse_helper(text, n + 1)

    return reverse_helper(text, 1)


def fib(n: int) -> int:
    if n < 0:
        sys.exit('Check ur code bruh')
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)



def nSums(n: int) -> int:

    def ile_cyfruni(n: int, i: int = 0) -> int:
        if n == 0:
            if i == 0:
                return 1
            return i
        return ile_cyfruni(int(n / 10), i + 1)

    def get_cyfrunie(n: int, i: int) -> int:
        divider = ile_cyfruni(n) - i
        return int((int(n / (10 ** divider))) % 10)

