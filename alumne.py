class alumne :
    def __init__(self,nom,nota,dni):
        alumne.nom = nom
        alumne.nota = nota
        alumne.dni = dni

    def aprovar(self) :
        if ( alumne.nota  >= 4.5 and alumne.nota < 5) :
            alumne.nota = 5

    def escriure(self) :
        print(alumne.nom,alumne.dni,alumne.nota,end ='')
        print('\n')
