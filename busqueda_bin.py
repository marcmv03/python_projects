
def binsearch(esq,dre,x,v) :
    global y
    if esq > dre:
        return 0

    else :
        m = (esq+dre)//2
        if x > v[m] :
            return binsearch(m+1,dre,x,v)
        elif x < v[m] :
            return binsearch(esq,m-1,x,v)
        else :
            y = m
            return 1

        return 0


v = []
n = input()
n = int(n)
i = 0
while i < n :
    x = input()
    x = int(x)
    v.append(x)
    i += 1

x = input()
x = int(x)
if binsearch(0,n-1,x,v) == 1 :
    print("trobat")
    print(y)
else :
    print("no trobat")
