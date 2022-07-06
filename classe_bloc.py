class Bloc :
    def __init__(self,tamany,etiq) :
        Bloc.contingut = []
        Bloc.tamany = tamany
        Bloc.etiq = etiq

    def escriure(self,valor) :
        self.contingut.append(valor)

    def  llegir(self) :
        print("etiqueta :",self.etiq,end='')
        for c in self.contingut :
            print(c)
