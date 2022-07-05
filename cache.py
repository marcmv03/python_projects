def char_to_hex(c) :
    if '0' <= c <= '9' :
        return int(c -'0')
    elif 'A' <= c <= 'F':
        return 10 +int(c -'A')

def hex_to_char(num) :
    if 0 <= num <= 9 :
        return str(num + '0')
    else :
        return str( num + 55)

def  dec (num) :
    p = 1
    r = 0
    i = len(num)-1
    while( i >= 0) :
        r = r +char_to_hex(num[i])*p
        p = 16*p
        i = i -1
    return r

def hex(num) :
    global l
    l = '0x'
    if num < 16 :
        return hex_to_char(num%16)
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

    def acces(self,adr) :
            adr = dec(adr)
            num_bloc = adr//Cache.t_bloc
            index = num_bloc % Cache.num_blocs
            etiq = num_bloc // Cache.num_blocs
            etiq = bin(etiq)
            print(etiq)
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
