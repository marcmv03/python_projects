def  dec (num) :
    p = 1
    r = 0
    i = len(num)-1
    while( i >= 0) :
        if num[i] == '1':
            r = r + p
        p = 2*p
        i = i -1
    print(r)
    return r

def bin(num,l) :
    if num < 2 :
     return num
    else :
     bin(num//2,l)
     if( num%2 == 1):
         return l + '1'
     else:
        return l +'0'



class Cache :
    def __init__(self,num_blocs,t_bloc,politica) :
         Cache.num_blocs = num_blocs
         Cache.t_bloc = t_bloc
         Cache.politica = politica
         Cache.contingut = {}

    def acces(self,adr) :
            adr = dec(adr)
            num_bloc = adr%Cache.num_blocs
            etiq = adr // Cache.num_blocs
            l = ''
            etiq = bin(etiq,l)
            print(etiq)
            if num_bloc in Cache.contingut :
                print("hit")
                return 1
            else :
                Cache.contingut[num_bloc] = etiq
                print("miss")
                return 0

    def escriure(self) :
        print(Cache.contingut)
