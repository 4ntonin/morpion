from file import CFile


class CMorpion:
    def __init__(self):
        self.__grille = [['-', '-', '-'],
                         ['-', '-', '-'],
                         ['-', '-', '-']]
        self.__joueur = 1
        self.__tour = 0
        self.__historique = CFile(9)

    def get_joueur(self):
        return self.__joueur
    
    def get_tour(self):
        return self.__tour

    def get_case(self, ligne, colonne):
        return self.__grille[ligne][colonne]

    def reset_grille(self):
        self.__grille = [['-', '-', '-'],
                         ['-', '-', '-'],
                         ['-', '-', '-']]

    def reset_joueur(self):
        self.__joueur = 1

    def changer_joueur(self):
        if self.__joueur == 1:
            self.__joueur = 2
        else:
            self.__joueur = 1

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
        Coup = CCoup()
        Coup.set_coup(self.__joueur, ligne, colonne)
        self.__historique.enfile(Coup)
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

    def rejouer(self):
        """rejoue la partie grâce à l'historique"""
        coupactuel = self.__historique.defile()
        self.jouer(coupactuel.get_ligne(), coupactuel.get_colonne())


class CCoup:
    def __init__(self):
        self.__ligneJouee = 0
        self.__colonneJouee = 0
        self.__joueuractif = 1

    def set_coup(self, joueur, ligne, colonne):
        self.__joueuractif = joueur
        self.__ligneJouee = ligne
        self.__colonneJouee = colonne

    def get_joueur(self):
        return self.__joueuractif

    def get_colonne(self):
        return self.__colonneJouee

    def get_ligne(self):
        return self.__ligneJouee


def afficher_grille():
    for i in range(3):
        for j in range(3):
            print(Morpion.get_case(i, j), ' ', end='')
        print('')


Morpion = CMorpion()

while Morpion.get_tour() != 9 and not Morpion.condition_fin():
    while not Morpion.jouer(int(input("Ligne ? ")), int(input("Colonne ? "))):
        print("Erreur, rejouez.")
    afficher_grille()
    Morpion.changer_joueur()
if not Morpion.condition_fin():
    print("Match nul !")
else:
    print("Le joueur " + str(Morpion.get_joueur()) + " a gagné !")
shistorique = str(input("Voulez-vous regarder l'historique ? (oui ou non) "))
nbcoups = Morpion.get_tour()
while shistorique == "oui":
    Morpion.reset_grille()
    Morpion.reset_joueur()
    coupactuel = 0
    affichercoupsuivant = "oui"
    while coupactuel < nbcoups and affichercoupsuivant == "oui":
        Morpion.rejouer()
        Morpion.changer_joueur()
        afficher_grille()
        coupactuel += 1
        if coupactuel < nbcoups:
            affichercoupsuivant = str(input("Voulez-vous afficher le coup suivant ? (oui ou non) "))
    if affichercoupsuivant == "oui":
        shistorique = str(input("Voulez-vous re-regarder l'historique ? (oui ou non) "))
    else:
        shistorique = "non"
