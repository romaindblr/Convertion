# crée par Romain Doublier-Villette
# convertisseur des nombres en décimal, binaire, hexadécimal et octal
class Convertion:

    def __init__(self):
        print("Bonjours !!")
        print("Bienvenue sur mon programme de Convertion")
        self.choix = 0
        self.resultat = 0
        self.resultat_decimal = 0
        self.resultat_binaire = 0
        self.resultat_hexa = 0
        self.resultat_octa = 0
        self.chiffre_convert = 0
        self.chiffre_start = 0
        self.cont = 0
        self.start_choix()

    def start_choix(self):
        # savoir ce qu'elle est son unité de départ
        print("§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§")
        print("Qu'elle est ton unité de départ :")
        print("1 = décimal")
        print("2 = binaire")
        print("3 = hexadécimal")
        print("4 = octal")
        self.choix = input("Fait ton choix : ")
        self.choix_verif()

    def choix_verif(self):
        # vérifie si son choix est correcte
        try :
            self.choix = int(self.choix)
        except:
            print("Aie tu t'ai tromper")
            self.start_choix()
        if self.choix == 1 or self.choix == 2 or self.choix == 3 or self.choix == 4:
            # choix correcte
            self.start_convertion()
        else:
            # choix pas correcte
            print("Aie tu t'ai tromper !!")
            self.start_choix()

    def start_convertion(self):
        # demande le chiffre qu'il veut convertire
        print("§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§")
        self.chiffre_start = input("Quels chiffre veut-tu convertir ? ")
        self.converte_chiffre()
        self.resultat_decimal = self.convertion(int, 1)
        self.resultat_binaire = self.convertion(bin, 2)
        self.resultat_hexa = self.convertion(hex, 2)
        self.resultat_octa = self.convertion(oct, 2)
        self.Print()
        self.Continue()

    def converte_chiffre(self):
        # verifie si le chiffre qu'il a mis correspond a l'unité qu'il a choisi
        if self.choix == 1:
            self.converte_chiffre_verif(10, "décimal")
        elif self.choix == 2:
            self.converte_chiffre_verif(2, "binaire")
        elif self.choix == 3:
            self.converte_chiffre_verif(16, "hexadecimal")
        elif self.choix == 4:
            self.converte_chiffre_verif(8, "octal")
        return

    def converte_chiffre_verif(self, unit, name_unit):
        try:
            self.chiffre_convert = int(self.chiffre_start, unit)
            return
        except:
            print("Aie ceci n'est pas du", name_unit)
            self.start_convertion()

    def convertion(self, unit, number):
        self.resultat = unit(self.chiffre_convert)
        if number == 2:
            self.resultat = self.resultat[2::]
        return self.resultat

    def Print(self):
        # affiche dans la console les résultat
        print("décimal :", self.resultat_decimal)
        print("binaire :", self.resultat_binaire)
        print("hexadécimal :", self.resultat_hexa)
        print("octal :", self.resultat_octa)

    def Continue(self):
        # savoir si il veut convertire d'autre chiffre
        try:
            print("§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§")
            print("Veut-tu continuer à convertire des chiffres ?")
            self.cont = int(input("1 = oui ; 2 = non : "))
        except:
            print("Aie ceci n'est pas un 1 ou un 2 !!")
            self.Continue()
        if self.cont == 1:
            print("§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§")
            self.start_choix()
        elif self.cont == 2:
            print("§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§")
            print("§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§")
            print("Au revoir !!")
            exit()
        else:
            print("Aie ceci n'est pas un 1 ou un 2 !!")
            self.Continue()

Convertion()
