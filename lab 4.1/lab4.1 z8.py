stopnie = (
 "Szeregowy",
 "Kapral",
 "Sierżancie",
 "Porucznik",
 "Kapitan",
 "Major",
 "Pułkownik",
)
# liczba stopni wojskowych
liczba_stopni = len(stopnie)

# indeks elementu 'Major'
Major_index = stopnie.index("Major")

# Czy pułkownik znajduję się w krotce
Pulkownik_wstepowanie = "Pułkownik" in stopnie

print(f"Liczba stopni wojskowych: {liczba_stopni}")
print(f"Indeks elementu Major: {Major_index}")
print(f"Czy Pułkownik znajduje się w krotce stopnie: {Pulkownik_wstepowanie}")