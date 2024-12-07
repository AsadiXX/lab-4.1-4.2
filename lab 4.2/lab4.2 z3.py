def powitanie(imie="Użytkowniku", jezyk="poslki"):
    if jezyk == "polski":
        print(f"Cześć, {imie}.")
    elif jezyk == "angielski":
        print(f"Hello, {imie}.")
    elif jezyk == "niemiecki":
        print(f"Guten Morgen, {imie}.")
    else:
        print(f"Witaj, {imie}.")

# Przykłady użycia funkcji
imie = input("Podaj swoje imię: ") or "Użytkowniku"
jezyk = input("Podaj język powitania (polski, angielski, niemiecki): ") or "polski"

powitanie(imie, jezyk)

# Podaj swoje imię: Piotr
# Podaj język powitania (polski, angielski, niemiecki): polski
# Cześć, Piotr.

# Podaj swoje imię: Steven
# Podaj język powitania (polski, angielski, niemiecki): angielski
# Hello, Steven.
