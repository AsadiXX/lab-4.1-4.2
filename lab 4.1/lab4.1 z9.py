lista_zakupow = {
    "Chleb": 4.5,
    "Woda": 3.2,
    "Masło": 8.0,
    "Szampon": 14.7,
    "Ser": 16.1
}

# Wyświetlenie listy zakupów
print("Lista zakupów:")
for artykul, kwota in lista_zakupow.items():
    print(f"{artykul}: {kwota} zł")

# Podsumowanie wydatków
suma_wydatkow = sum(lista_zakupow.values())
print(f"Suma wydatków: {suma_wydatkow} zł")