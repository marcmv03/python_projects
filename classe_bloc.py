class bloc :
    def __init__(self,tamany) :
        Bloc.contingut = []
        Bloc.tamany = tamany

    def escriure(self,valor) :
        self.contingut.append(valor)

    def  escriure(self) :
        for c in self.contingut :
            print(c)
