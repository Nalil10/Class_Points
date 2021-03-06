import math
import os
import turtle as ttl
import random as rd
import __function__ as fonc

class Vecteur:
    def __init__(self, dictVecteur={}, name="", x=0, y=0):
        self.name = name
        self.x = x
        self.y = y
        self.norme = math.sqrt((self.x)**2 + (self.y)**2)
        if self.name != "":
            dictVecteur[self.name] = self
    def __str__(self):
        return "({0},{1})".format(self.x, self.y)
    def random(self, nameList, dictVecteur={}):
        """
        Redefinit les caracteristiques du vecteur aleatoirement
        """ 
        nameNumber = rd.randint(0, len(nameList))
        self.name = nameList[nameNumber-1]
        del nameList[nameNumber-1]
        self.x = rd.randint(-250,250)
        self.y = rd.randint(-250,250)
        self.norme = math.sqrt((self.x)**2 + (self.y)**2)
        dictVecteur[str(self.name)] = self
        return self
    def __add__(self, other):
        return Vecteur(self.x + other.x, self.y + other.y)
    def __mul__(self, k):
        return Vecteur(self.x * k, self.y * k)
    def __rmul__(self, k):
        return Vecteur(self.x * k, self.y * k)
    def tracage(self, dictVecteur={}, information= "O"):
        """
        Trace le vecteur
        """
        tortue = fonc.tortue()
        tortue.up()
        tortue.home()
        tortue.down()
        tortue.goto(self.x,self.y)
        tortue.up()
        if information == "O":
            tortue.write("V[" + str(self.name) + "]" + "\n" + "(" + str(round(self.x, 1)) + ";" + str(round(self.y, 1)) + ")")
        if self.y >= 0:
            tortue.left(self.angle_degree(Vecteur(dictVecteur, "", 100,0)))
        if self.y <= 0:
            tortue.right(self.angle_degree(Vecteur(dictVecteur, "", 100,0)))
        fichier = open("data.txt", 'a')
        fichier.write("V[" + str(self.name) + "] : (" + str(round(self.x, 1)) + ";" + str(round(self.y, 1)) + ")" + "\n")
        fichier.close()
    def colineaire(self, other):
        """
        Verifie si deux vecteurs sont colinéaires, renvoie True si c'est vrai, sinon renvoie False
        """
        try:
            k = [self.x/other.x, self.y/other.y]
        except ZeroDivisionError:
            if other.x == 0 and other.y != 0:
                k = [0, self.y/other.y]
            elif other.y == 0 and other.x != 0:
                k = [self.x/other.x, 0]
            elif other.x == 0 and other.y == 0:
                k = [0,0]
        if k[0] == k[1] or k[0] == 0 or k[1] == 0:
            return True
        else:
            return False
    def produit_scalaire(self, other):
        """
        Calcule le produit scalaire de deux vecteurs
        """
        return self.x * other.x + self.y * other.y
        #return fonc.int_decimal(1/2*((self.norme)**2 + (other.norme)**2 - round(((self+other).norme)**2, 4)))
    def angle_degree(self, other):
        """
        Definit l'angle entre deux vecteurs en degree
        """
        try:
            return math.degrees(math.acos((self.produit_scalaire(other))/(self.norme * other.norme)))
        except ZeroDivisionError:
            return None # Car c'est un point
    def angle_radian(self, other):
        """
        Definit l'angle entre deux vecteurs en radian
        """
        return math.acos((self.produit_scalaire(other))/(self.norme * other.norme))


if __name__ == "__main__":
    print("Lancement du module __Vecteur__ en cours...")
    fonc.clear_data()
    dictVecteur = fonc.dictionnary_vecteur()
    nameList = fonc.liste_name(2)
    a = Vecteur(dictVecteur)
    a.random(nameList, dictVecteur)
    b = Vecteur(dictVecteur, nameList[0], 0.5*a.x, 0.5*a.y)
    a.tracage(dictVecteur)
    b.tracage(dictVecteur)
    print(dictVecteur)
    print("Fin du module.")
    while 1:
        os.system("pause")