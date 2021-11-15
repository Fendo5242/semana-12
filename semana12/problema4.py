def esVocal(vocal):
    vocales = ["a", "e", "i", "o", "u"]
    if vocal in vocales:
        return True
    else:
        return False
vocal = input("Ingrese una vocal: ")
print(esVocal(vocal))
