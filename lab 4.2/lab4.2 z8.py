# A.
def wyswietl_parametry(*args):
    print("Przekazane parametry:")
    for arg in args:
        print(arg)

wyswietl_parametry(1, "tekst", 3.14, True)
