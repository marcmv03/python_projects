import numpy as np
class Bloc :
    def __init__(self,tamany,etiq) :
        Bloc.contingut = np.zeros(tamany,dtype = int)
        Bloc.etiq = etiq

    def escriure(self,valor,offsett) :
        self.contingut[offsett] = valor

    def  llegir(self) :
        print("etiqueta: ",self.etiq,'\n',end='')
        for c in self.contingut :
            print(c)
