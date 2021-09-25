# cree par Romain Doublier-villette
# convertisseur nombre base 10 en binaire et inversement

def __init__():
    print("Bonjours !!")
    print("Bienvenue sur mon programme de convertion")
    start()

def start():
    # savoir ce qu'i veut convertire et en quoi
    chiffre_convert = input("Qu'elle chiffre veut-tu convertir ? ")
    chiffre_convert_d = convert1(chiffre_convert)
    chiffre_convert = chiffre_convert_d
    chiffre_convert_b = binaire(chiffre_convert)
    chiffre_convert_x = hexadecimal(chiffre_convert)
    print("décimal :",chiffre_convert_d)
    print("binaire :", chiffre_convert_b)
    print("hexadécimal :", chiffre_convert_x)
    Continue()

def binaire(chiffre_convert):
    # convertire en binaire
    chiffre_convert_b = bin(chiffre_convert)
    Resultat = chiffre_convert_b[2::]
    return Resultat

def decimal(chiffre_convert):
    # convertire en décimal
    chiffre_convert_d = int(chiffre_convert)
    Resultat = chiffre_convert_d
    return Resultat

def hexadecimal(chiffre_convert):
    # convertire en hexadécimal
    chiffre_convert_x = hex(chiffre_convert)
    Resultat = chiffre_convert_x[2::]
    return Resultat

def Continue():
    # savoir si il veut convertire d'autre chiffre
    cont = int(input("Veut-tu continuer a convertire des nombres ? 1 = oui ; 2 = non : "))
    if cont == 1:
        start()
    else:
        print("au revoir !!")
        exit()

def convert1(chiffre_convert):
    try:
        chiffre_convert_d = int(chiffre_convert, 2)
        a = decimal(chiffre_convert_d)
        return a
    except:
        a = convert2(chiffre_convert)
        return a

def convert2(chiffre_convert):
    try:
        chiffre_convert_d = int(chiffre_convert)
        a = decimal(chiffre_convert_d)
        return a

    except:
        chiffre_convert_d = int(chiffre_convert, 16)
        a = decimal(chiffre_convert_d)
        return a

__init__()