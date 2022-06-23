def binsearch(esq,dre,x,v) :
    if esq > dre:
        return 0

    else :
        m = int((esq+dre)/2)
        if v[m] > x : return binsearch(m+1,dre,x,v)
        elif v[m] < x : return binsearch(esq,m-1,x,v)
        else : return 1



v = []
n = input()
n = int(n)
i = 0
while i < n :
    x = input()
    x = int(x)
    v.append(x)
    ++i

x = input()
x = int(x)
if binsearch(0,n-1,x,v) == 1 :
    print("trobat")
else :
    print("no trobat")
