def znajdz_maksimum(*args):
    if not args:
        return "Nie przekazano żadnych argumentów."

    maksimum = max(args)
    return maksimum

wynik = znajdz_maksimum(12, 47, 45, 167, 23)
print(f"Maksymalna wartość: {wynik}")
