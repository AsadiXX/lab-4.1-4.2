def fibonacci(n):
    if n == 0:  # Warunek bazowy
        return 0
    elif n == 1:  # Warunek bazowy
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)  # Rekurencja

try:
    n = int(input("Podaj numer wyrazu ciągu Fibonacciego (n >= 0): "))
    if n < 0:
        print("Numer wyrazu musi być większy lub równy 0")
    else:
        wynik = fibonacci(n)
        print(f"{n}-ty wyraz ciągu Fibonacciego to: {wynik}")
except ValueError:
    print("Błąd: Podaj liczbę całkowitą!")