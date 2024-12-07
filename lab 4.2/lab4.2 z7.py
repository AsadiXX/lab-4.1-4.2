def potega(a, n):

    if n == 0:
        return 1
    elif n > 0:
        return a * potega(a, n - 1)
    else:  # n < 0
        return 1 / potega(a, -n)

try:
    podstawa = float(input("Podaj podstawę potęgi (a): "))
    wykladnik = int(input("Podaj wykładnik potęgi (n): "))
    wynik = potega(podstawa, wykladnik)
    print(f"Wynik {podstawa}^{wykladnik} = {wynik:.6f}")
except ValueError:
    print("Błąd: Wprowadzono nieprawidłowe dane.")
except Exception as e:
    print(f"Nieoczekiwany błąd: {e}")