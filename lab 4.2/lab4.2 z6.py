import math
def pole_trojkata(a, b, c):

    try:
        # Konwersja na liczby float
        a = float(a)
        b = float(b)
        c = float(c)

        # Sprawdzenie poprawności danych
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError("Długości boków muszą być większe od zera.")
        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError("Podane długości boków nie tworzą trójkąta.")

        # Obliczanie półobwodu
        s = (a + b + c) / 2

        # Obliczanie pola trójkąta za pomocą wzoru Herona
        pole = math.sqrt(s * (s - a) * (s - b) * (s - c))
        return pole

    except ValueError as ve:
        return f"Błąd danych: {ve}"
    except Exception as e:
        return f"Nieoczekiwany błąd: {e}"

try:
    bok_a = input("Podaj długość boku a: ")
    bok_b = input("Podaj długość boku b: ")
    bok_c = input("Podaj długość boku c: ")

    wynik = pole_trojkata(bok_a, bok_b, bok_c)
    if isinstance(wynik, float):
        print(f"Pole trójkąta wynosi: {wynik:.2f}")
    else:
        print(wynik)
except Exception as e:
    print(f"Nieoczekiwany błąd w programie: {e}")