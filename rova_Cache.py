from cache import *

print("num blocs")
n = int(input())
print("tamany bloc")
t = int(input())
print("politica d'escriptura")
pol = int(input())
c = Cache(n,t,pol)
adr = str(input())
h = 0
m = 0
while(adr != "fi") :
    print("lectura : 0 , escriptura : 1")
    mod = int(input())
    c.acces(adr)
    adr = str(input())
c.escriure()
