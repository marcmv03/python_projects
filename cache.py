from classe_bloc import *

def char_to_hex(c) :
    if '0' <= c <= '9' :
        return int(c)
    elif 'A' <= c <= 'F':
        return int(10 + ord(c) - 65)

def hex_to_char(num) :
    if 0 <= num <= 9 :
        return str(num)
    else :
        return chr( num + 55)

def  dec (num) :
    p = 1
    r = 0
    i = len(num)-1
    while( i >= 0) :
        if num[i] == '1':
            r = r + p
        p = 2*p
        r = r +char_to_hex(num[i])*p
        p = 16*p
        i = i -1
    return r

def hex(num) :
    global l
    l = '0x'
    if num < 16 :
        l = l + hex_to_char(num)
        return hex_to_char(num)
    else :
        hex(num//16)
        l = l + hex_to_char(num%16)

    return l



class Cache :
    def __init__(self,num_blocs,t_bloc,politica) :
         Cache.num_blocs = num_blocs
         Cache.t_bloc = t_bloc
         Cache.politica = politica
         Cache.contingut = {}

    def acces(self,adr,mod) :
            valor = 0
            adr = dec(adr)
            print(adr)
            num_bloc = adr//Cache.t_bloc
            index = num_bloc % Cache.num_blocs
            etiq = num_bloc // Cache.num_blocs
            etiq = hex(etiq)
            if (index in Cache.contingut and Cache.contingut[index].etiq == etiq) :
                print("hit")
                return True
            else :

                if Cache.politica == 1:
                    Cache.contingut[index] = Bloc(self.t_bloc,etiq)
                print("miss"."escriptura a memoria")
                return False
            if(mod == 1) :
                    print("Escriptura a  memoria")
                    valor = int(input("escriu valor : "))
                    self.contingut[index].escriure()
    def buidar(self) :
        self.contingut.clear()

    def escriure_contingut_bloc(self,i) :
        print("contingut bloc",i,end =" ")
        if i in self.contingut :
            self.contingut[i].llegir()
        else :print("bloc buit")

    def escriure(self) :
        for i in range(Cache.num_blocs) :
            if i in Cache.contingut :
                print("Bloc",i, ':' ,Cache.contingut[i].etiq,end = ' ')
                print('\n')
            else :
                print("Bloc" ,i,':',"buit",end = ' ')
                print('\n')
