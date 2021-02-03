class CMorpion:
    def __init__(self):
        self.__grille = [['-', '-', '-'],
                         ['-', '-', '-'],
                         ['-', '-', '-']]
        self.__joueur = 1
        self.__tour = 0
        self.__file = CFile(9)

    def get_joueur(self):
        return self.__joueur
    
    def get_tour(self):
        return self.__tour

    def get_case(self, ligne, colonne):
        return self.__grille[ligne][colonne]

    def changer_joueur(self):
        if Morpion.__joueur == 1:
            Morpion.__joueur = 2
        else:
            Morpion.__joueur = 1

    def jouer(self, ligne, colonne):
        """vérifie si les lignes et colonnes entrées par le joueur peuvent être placées dans la grille"""
        if ligne > 3 or ligne < 1 or colonne > 3 or colonne < 1:
            return False
        if self.__grille[ligne - 1][colonne - 1] != '-':
            return False
        if self.__joueur == 1:
            self.__grille[ligne - 1][colonne - 1] = 'X'
        else:
            self.__grille[ligne - 1][colonne - 1] = 'O'
        self.__tour += 1
        return True

    def condition_fin(self):
        """conditions pour que quelqu'un gagne"""
        for i in range(3):
            if self.__grille[i][0] == self.__grille[i][1] == self.__grille[i][2] != '-':
                return True
        for i in range(3):
            if self.__grille[0][i] == self.__grille[1][i] == self.__grille[2][i] != '-':
                return True
        if self.__grille[0][0] == self.__grille[1][1] == self.__grille[2][2] != '-':
            return True
        if self.__grille[0][2] == self.__grille[1][1] == self.__grille[2][0] != '-':
            return True
        return False


Morpion = CMorpion()

while Morpion.get_tour() != 9 and not Morpion.condition_fin():
    while Morpion.jouer(int(input("Ligne ? ")), int(input("Colonne ? "))) == False:
        print("Erreur, rejouez.")
    for i in range(3):
        for j in range(3):
            print(Morpion.get_case(i, j), ' ' , end='')
        print('')
    Morpion.changer_joueur()
if not Morpion.condition_fin():
    print("Match nul !")
else:
    print("Le joueur " + str(Morpion.get_joueur()) + " a gagné !")
