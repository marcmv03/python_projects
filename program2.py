from alumne import *

nom = input()
dni = input()
nota = float(input())
alum = alumne(nom,nota,dni)
alum.aprovar()
alum.escriure()
