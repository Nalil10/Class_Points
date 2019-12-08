import math
import os

class Vecteur:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.norme = math.sqrt(self.x**2 + self.y**2)
    def __str__(self):
        return "({0},{1})".format(self.x, self.y)
    def __add__(self, other):
        return Vecteur(self.x + other.x, self.y + other.y)
    def colinéaire(self, other):
        try:
            k = [self.x/other.x, self.y/other.y]
        except ZeroDivisionError:
            if other.x == 0:
                k[0] = 0
            if other.y == 0:
                k[1] = 0
        return tuple(k)
    def produit_scalaire(self, other):
        print(((self+other).norme)**2)
        produitScalaire = 1/2*(self.norme**2 + other.norme**2 - ((self+other).norme)**2) 
        return produitScalaire

if __name__ == "__main__":
    print("Lancement du module __classe__ en cours...")
    a = Vecteur(1,0)
    b = Vecteur(2,0)
    print(a.colinéaire(b))
    #print(a.produit_scalaire(b))
    #print(b.produit_scalaire(a))
    print("Fin du module.")
    while 1:
        os.system("pause")