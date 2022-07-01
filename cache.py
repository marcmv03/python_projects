class Cache :
    def__init__(self,num_blocs,t_bloc,politica) ;
         Cache.num_blocs = num_blocs
         Cache.t_bloc = t_bloc
         Cache.politica = politica
         Cache.contingut = {}


    def __dec(num):
        p = 1
        num = 0
        for i in range(len(num),0):
            num = num + p*num[i]
            p = 2*p
        return num

    def __bin(num,l) :
        if num < 2 :
            return num
        else :
            return [num%2] + bin(num//2,l)



    def acces(self,adr) :
            adr = dec(adr)
            num_bloc = adr%Cache.num_blocs
            etiq = adr // Cache.num_bloc
            etiq = bin(etiq)
            if etiq in Cache.contingut :
                print("hit")
                return true
            else :
                Cache.contingut[num_bloc] = etiq
                print("miss")
                return false

        def escriure() :
            for element in contingut :
                print(key,'=',value,end = '')
