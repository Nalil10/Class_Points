import __Point__ as cp
import __function__ as fonc
import turtle as ttl
import os
import math


class Polynome:
    def __init__(self, *coef):
        self.coef = coef

        chaine = ""
        if type(self.coef[0]) == list:
            self.coef = list(self.coef)
            otherKick = list(self.coef[0])
            del self.coef[0]
            for element in otherKick:
                self.coef.append(element)
            self.coef = tuple(self.coef)
        for element in range(0, len(self.coef)):
            i =  -(element-(len(self.coef)-1)) 
            if element == len(self.coef)-1:
                if self.coef[element] < 0:
                    chaine += "(" + str(self.coef[element]) + ")"
                else:
                    chaine += str(self.coef[element])
            elif self.coef[element] < 0:
                chaine += "(" + str(self.coef[element]) + ")*x**" + str(i) + "+"
            else:
                chaine += str(self.coef[element]) + "*x**" + str(i) + "+"
        self.chaine = chaine
    def __str__(self):
        chaine = ""
        if type(self.coef[0]) == list:
            self.coef = list(self.coef)
            otherKick = list(self.coef[0])
            del self.coef[0]
            for element in otherKick:
                self.coef.append(element)
            self.coef = tuple(self.coef)
        for element in range(0, len(self.coef)):
            if type(self.coef[element]) == list:
                self.coef = list(self.coef)
                coefKick = list(self.coef[element])
                del self.coef[element]
                for element in coefKick:
                    self.coef.append(element)
                self.coef = tuple(self.coef)
            i =  -(element-(len(self.coef)-1)) 
            if element == len(self.coef)-1:
                if self.coef[element] < 0:
                    chaine += "(" + str(self.coef[element]) + ")"
                else:
                    chaine += str(self.coef[element])
            elif self.coef[element] < 0:
                chaine += "(" + str(self.coef[element]) + ")x**" + str(i) + "+"
            else:
                chaine += str(self.coef[element]) + "x**" + str(i) + "+"
        return chaine
    def y(self,x):
        """
        Renvoie l'ordonnee (y) de la fonction avec comme paramètre x etant definit dans l'argument
        """
        if x < 0:
            x = "(" + str(x) + ")"
        return eval(self.chaine.replace("x", str(x)))
    def x(self,y):
        """
        Renvoie l'abscisse (x) de la fonction avec comme paramètre y (donc f(x)) etant definit dans l'argument
        Non fini
        """
        if len(self.coef) == 2: #Fonction affine
            return eval("("+"(-" + str(self.coef[1]) +")+"+ "("+str(y)+")" + ")/("+ str(self.coef[0]) +")")
        if len(self.coef) == 3: #Fonction du second degré
            discriminant = (self.coef[1])**2 - 4*(self.coef[0])*(self.coef[2])
            if discriminant > 0:
                x1 = ((-(self.coef[1]))-math.sqrt(discriminant))/(2*(self.coef[0]))
                x2 = ((-(self.coef[1]))+math.sqrt(discriminant))/(2*(self.coef[0]))
                return x1,x2
            elif discriminant < 0:
                discriminant = "1j*math.sqrt("+ str(discriminant*(-1)) + ")"
                z1 = str(-(self.coef[1])) + "-" + discriminant + "/" + str((2*(self.coef[0])))
                z2 = str(-(self.coef[1])) + "+" + discriminant + "/" + str((2*(self.coef[0])))
                return z1,z2
            elif discriminant == 0:
                x1 = (-(self.coef[1]))/(2*(self.coef[0]))
                x2 = (-(self.coef[1]))/(2*(self.coef[0]))
                return x1,x2

    def extremum(self):
        """
        Renvoie l'abscisse et l'ordonnee de l'extremum de la fonction
        """
        if "x**2" in self.chaine:
            alpha = (-self.coef[1])/(2*self.coef[0])
            strAlpha = "(" + str(alpha) + ")"
            beta = eval(self.chaine.replace("x", strAlpha))
            return (alpha, beta)
    def tracage(self):
        """
        Trace la fonction
        """
        tortue = fonc.tortue()
        tortue.speed(0)
        tortue.up()
        precision = 1800*2 # 1800 precision normale avec un tracage de 1x par 1x 
        for i in range(-precision,precision):
            u = i*(1800/precision)
            print(str(u) + " " + str(self.y(u)))
            tortue.goto(u, self.y(u))
            tortue.down()
            tortue.ht()
        tortue.up()
    def derive(self, nombre_derive=1):
        """
        Cree la derivee de la fonction
        """
        coefDerive = []
        for element in range(len(self.coef)-1):
            n = -(element-(len(self.coef)-1))
            coefDerive.append(n*self.coef[element])
        derive = Polynome(coefDerive)
        for i in range(nombre_derive-1):
            i = i
            derive = derive.derive()
        return derive
    def tangente(self, a):
        derive = self.derive()
        tangente = str(derive.y(a)) + "*" +  "(x-" + "(" + str(a) + ")" + ")" + "+" + str(self.y(a))
        tortue = fonc.tortue()
        tortue.speed(0)
        tortue.up()
        precision = 1*2 # 1800 precision normale avec un tracage de 1x par 1x 
        for i in range(-precision,precision):
            u = i*(1800/precision)
            print(str(u) + " " + str(eval(tangente.replace("x", str(u)))))
            tortue.goto(u, eval(tangente.replace("x", str(u))))
            tortue.down()
            tortue.ht()
        tortue.up()
        return tangente
    def factorisation(self):
        """
        Renvoie en string la factorisation de la fonction
        """
        facteur = str()
        for index in range(1,len(self.coef),2):
            facteur += "(" + str(self.coef[index]) + ")*"
        return facteur




if __name__ == "__main__":
    print("Lancement du module __Fonction__ en cours...")
    fonc.repere(fonc.tortue())
    f = Polynome(4,1,2)
    for i in range(-1, 1):
        i *= 100
        print(f.tangente(i))
        f.tangente(i)
    print("Fin du module.")
    while 1:
        os.system("pause")