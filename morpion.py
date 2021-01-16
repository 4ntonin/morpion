class CMorpion:
    def __init__(self):
        self.grille = [['-', '-', '-'],
                       ['-', '-', '-'],
                       ['-', '-', '-']]
        self.joueur = 0
        self.tour = 0
        self.verif_tour = 0

    def afficher_grille(self):
        """affiche la grille"""
        for i in range(3):
            print(self.grille[i])

    def verification(self, ligne, colonne):
        """vérifie si les lignes et colonnes entrées par le joueur peuvent être placées dans la grille"""
        self.verif_tour += 1
        if 0 > ligne > 3 or 0 > colonne > 3:
            return print("Erreur, re-essayez.")
        if self.grille[ligne - 1][colonne - 1] != '-':
            return print("Erreur, re-essayez.")
        self.jouer(ligne, colonne)

    def jouer(self, ligne, colonne):
        """change l'endroit de la grillle voulu par le joueur en 'X' ou 'O' selon qui joue"""
        if self.joueur == 1:
            self.grille[ligne - 1][colonne - 1] = 'X'
        else:
            self.grille[ligne - 1][colonne - 1] = 'O'
        self.afficher_grille()
        self.tour += 1

    def lancer_partie(self):
        """lance la partie"""
        while self.joueur != 1 and self.joueur != 2:
            self.joueur = int(input("Quel joueur commence (1 ou 2) : "))
        while self.tour != 9:
            self.verif_tour = self.tour
            self.verification(int(input("Ligne ? ")), int(input("Colonne ? ")))
            if self.condition_fin():
                print("Le joueur " + str(self.joueur) + " a gagné !")
                break
            if self.verif_tour == self.tour:
                if self.joueur == 1:
                    self.joueur = 2
                else:
                    self.joueur = 1
        if not self.condition_fin():
            print("Match nul !")

    def condition_fin(self):
        """conditions pour que quelqu'un gagne"""
        for i in range(3):
            if self.grille[i][0] == self.grille[i][1] == self.grille[i][2] != '-':
                return True
        for i in range(3):
            if self.grille[0][i] == self.grille[1][i] == self.grille[2][i] != '-':
                return True
        if self.grille[0][0] == self.grille[1][1] == self.grille[2][2] != '-':
            return True
        if self.grille[0][2] == self.grille[1][1] == self.grille[2][0] != '-':
            return True
        return False


Morpion = CMorpion()
Morpion.lancer_partie()
