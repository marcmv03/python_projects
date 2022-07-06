from cache import  Cache
print("num blocs")
n = int(input())
print("tamany bloc")
t = int(input())
print("politica d'escriptura:")
print(" 0: sense assignacio ,1 : amb assignacio")

print("politica d'escriptura")

pol = int(input())
c = Cache(n,t,pol)
h = 0
m = 0
a = 0
op = str(input("comanda: "))
while(op != "fi") :
    if( op == "acces") :
        print("lectura : 0 , escriptura : 1")
        mod = int(input())
        adr = str(input("adr(hex)"))
        r =c.acces(adr,mod)
        if(r) :
            h +=1
        else:
            m += 1
        a += 1
    elif op == "etiquetes" :
        print("contingut_cache:")
        c.escriure()
    elif op =="llegir_bloc":
        i = int(input())
        c.escriure_contingut_bloc(i)
    elif op =="buidar" :
        c.buidar()

    op = str(input("comanda: "))


print("hit rate =",round(h/a,3),'\n',"miss rate =",round(m/a,3),'\n',end = '')
