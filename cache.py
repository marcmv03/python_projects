def  dec (num) :
    p = 1
    r = 0
    i = len(num)-1
    while( i >= 0) :
        if num[i] == '1':
            r = r + p
        p = 2*p
        i = i -1
    return r

def bin(num) :
    global l
    l = ''
    if num < 2 :
        if num == 0 :
            l = l +'0'
        else :
            l = l +'1'
        return l
    else :
        bin(num//2)
        if( num%2 == 1):
         l = l +'1'
         return l
        else:
         l = l +'0'
         return l



class Cache :
    def __init__(self,num_blocs,t_bloc,politica) :
         Cache.num_blocs = num_blocs
         Cache.t_bloc = t_bloc
         Cache.politica = politica
         Cache.contingut = {}

    def acces(self,adr,mod) :
            adr = dec(adr)
            num_bloc = adr//Cache.t_bloc
            index = num_bloc % Cache.num_blocs
            etiq = num_bloc // Cache.num_blocs
            etiq = bin(etiq)
            print(etiq)
            if mod == 1 :
                print("Escriptura a memoria")
            if (index in Cache.contingut and Cache.contingut[index] == etiq) :
                print("hit")
                return True
            else :
                if( Cache.politica == 1):
                    Cache.contingut[index] = etiq
                print("miss")
                return False

    def escriure(self) :
        for i in range(Cache.num_blocs) :
            if i in Cache.contingut :
                print("Bloc",i, ':' ,Cache.contingut[i],end = ' ')
                print('\n')
            else :
                print("Bloc" ,i,':',"buit",end = ' ')
                print('\n')
