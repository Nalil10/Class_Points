import __function__  as fonc
import __classe__ as cl
import os

fonc.clear_data()
fonc.repere(fonc.tortue())
dictMilieu = fonc.dictionnary_milieu()
"""
liste = []
for point in range(4):
    p = cl.Point()
    p.random()
    p.tracer()
    liste.append(p)

if len(liste) == 1:
    liste[0].liage(liste)
    liste[0].milieu(liste)
else:
    liste[0].liage(liste[1:len(liste)], liste[0])
    liste[0].milieu(liste[1:])
"""
a = cl.Point()
a.random()
a.tracer()

b = cl.Point()
b.random()
b.tracer()

a.liage(b)
while 1:
    os.system("pause")
