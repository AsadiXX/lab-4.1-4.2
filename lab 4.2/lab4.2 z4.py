def oblicz_srednia(lista_liczb):
    if not lista_liczb:  # Sprawdzenie, czy lista nie jest pusta
        return None
    return sum(lista_liczb) / len(lista_liczb)

liczby = [17, 47, 35, 67, 87]  # Lista liczb
srednia = oblicz_srednia(liczby)
print(f"Średnia z liczb {liczby} wynosi {srednia}")

pusta_lista = []
srednia_pusta = oblicz_srednia(pusta_lista)
print(f"Średnia z pustej listy: {srednia_pusta}")
