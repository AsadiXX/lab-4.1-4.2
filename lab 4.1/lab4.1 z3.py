# a. Wczyta (zmienną) imię oraz wyświetli tekst „Witaj” oraz wczytane imię.
imie = input("Podaj imię: ")
print (f"Witaj {imie}")

#b. Wczyta (zmienną) wiek oraz wyświetli tekst „Twój wiek to:” oraz wczytany wiek
wiek = input("Podaj wiek: ")
print(f"Twój wiek to {wiek} lat")

#c. Wczyta (zmienne) imię i nazwisko i wyświetli inicjały.
nazwisko = input("Podaj nazwisko: ")
print(f"Twoje inicjały to: ",imie[:1] , nazwisko[:1] )

# d. Wczyta łańcuch i wyświetli go pięć razy
text = input("Podaj łańcuch: ")
print((text + "\n") * 5)

# e. Wczyta dwa łańcuchy, a w trzecim łańcuchu zapamięta połączone te dwa łańcuchy
text1 = input("Podaj pierwszy łańcuch: ")
text2 = input("Podaj drugi łańcuch: ")
combined_text = text1 + text2
print("Połączony łańcuch:", combined_text)

# f. Wczyta dwa łańcuchy, a w trzecim łańcuchu zapamięta pierwszą połowę pierwszego i drugą połowę drugiego
text1 = input("Podaj pierwszy łańcuch: ")
text2 = input("Podaj drugi łańcuch: ")

# Obliczanie połówek
half1 = text1[:len(text1)//2]  # Pierwsza połowa pierwszego łańcucha
half2 = text2[len(text2)//2:]  # Druga połowa drugiego łańcucha


# Łączenie wyników
result = half1 + half2
print("Połączony wynik:", result)

