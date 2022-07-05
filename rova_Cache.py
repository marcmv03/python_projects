from cache import class Cache
print("num blocs")
n = int(input())
print("tamany bloc")
t = int(input())
print("politica d'escriptura:")
print(" 0: sense assignacio ,1 : amb assignacio")

print("politica d'escriptura")

pol = int(input())
c = Cache(n,t,pol)
adr = str(input("adr(hex)"))
h = 0
m = 0
a = 0
while(adr != "fi") :
    print("lectura : 0 , escriptura : 1")
    mod = int(input())
    r =c.acces(adr)
    if(r) :
        h +=1
    else:
        m += 1
    a += 1
    adr = str(input("adr"))
print("Contingut cache :")
c.escriure()
print("hit rate =",round(h/a,3),'\n',"miss rate =",round(m/a,3),'\n',end = '')
