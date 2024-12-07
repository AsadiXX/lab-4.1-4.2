# Definicja funkcji
def oblicz_kwadrat(liczba):
    return liczba ** 2

# Pobranie liczby od użytkownika
liczba = float(input("Podaj liczbę: "))

# Wywołanie funkcji i wyświetlenie wyniku
kwadrat = oblicz_kwadrat(liczba)
print(f"Kwadrat liczby {liczba} wynosi {kwadrat}.")
