def oblicz_bmi(waga, wzrost):

    bmi = waga / (wzrost ** 2)

    if bmi < 16:
        kategoria = "Niedowaga III stopnia"
    elif 16 <= bmi < 17:
        kategoria = "Niedowaga II stopnia"
    elif 17 <= bmi < 18.5:
        kategoria = "Niedowaga I stopnia"
    elif 18.5 <= bmi < 25:
        kategoria = "Pożądana masa ciała"
    elif 25 <= bmi < 30:
        kategoria = "Nadwaga"
    elif 30 <= bmi < 35:
        kategoria = "Otyłość I stopnia"
    elif 35 <= bmi < 40:
        kategoria = "Otyłość II stopnia"
    else:
        kategoria = "Otyłość III stopnia"

    return bmi, kategoria

waga = float(input("Podaj wagę w kilogramach: "))
wzrost = float(input("Podaj wzrost w metrach: "))
bmi, kategoria = oblicz_bmi(waga, wzrost)

print(f"Twoje BMI wynosi: {bmi:.2f}")
print(f"Kategoria: {kategoria}")