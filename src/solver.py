# -*-coding: utf8-*-

class SudokuSolver:
    """Cette classe permet d'explorer les solutions d'une grille de Sudoku pour la résoudre.
    Elle fait intervenir des notions de programmation par contraintes
    que vous n'avez pas à maîtriser pour ce projet."""

    def __init__(self, grid):
        """À COMPLÉTER
        Ce constructeur initialise une nouvelle instance de solver à partir d'une grille initiale.
        Il construit les ensembles de valeurs possibles pour chaque case vide de la grille,
        en respectant les contraintes définissant un Sudoku valide.
        Ces contraintes seront appliquées en appelant la méthode ``reduce_all_domains``.
        :param grid: Une grille de Sudoku
        :type grid: SudokuGrid
        """
        self.grid = grid
        self.possiblesChoices = []
        self.reduce_all_domains()

        # raise NotImplementedError()

    def reduce_all_domains(self):
        """À COMPLÉTER
        Cette méthode devrait être appelée à l'initialisation
        et élimine toutes les valeurs impossibles pour chaque case vide.
        *Indication: Vous pouvez utiliser les fonction ``get_row``, ``get_col`` et ``get_region`` de la grille*
        """

        vide = self.grid.get_empty_pos()

        for a in range(len(vide)):
            i = vide[a][0]
            j = vide[a][1]

            if i < 3:
                reg_i = 0
            elif i < 6:
                reg_i = 1
            else:
                reg_i = 2

            if j < 3:
                reg_j = 0
            elif j < 6:
                reg_j = 1
            else:
                reg_j = 2

            sList = set(range(1, 10))
            possibleLines = set(self.grid.get_row(i))
            possibleCol = set(self.grid.get_col(j))
            possibleReg = set(self.grid.get_region(reg_i, reg_j))
            listPossibles = list(sList - possibleCol - possibleLines - possibleReg)

            if len(listPossibles) == 0:
                print("Pas de Possibilités pour [" + str(i) + "][" + str(j) + "]")
            else:
                for i in range(len(listPossibles)):
                    self.possiblesChoices.append((i, j, listPossibles))

    # raise NotImplementedError()

    def reduce_domains(self, last_i, last_j, last_v):
        """À COMPLÉTER
        Cette méthode devrait être appelée à chaque mise à jour de la grille,
        et élimine la dernière valeur affectée à une case
        pour toutes les autres cases concernées par cette mise à jour (même ligne, même colonne ou même région).
        :param last_i: Numéro de ligne de la dernière case modifiée, entre 0 et 8
        :param last_j: Numéro de colonne de la dernière case modifiée, entre 0 et 8
        :param last_v: Valeur affecté à la dernière case modifiée, entre 1 et 9
        :type last_i: int
        :type last_j: int
        :type last_v: int
        """

        for case in self.possiblesChoices:

            coini = case[0] // 3
            coinj = case[1] // 3
            regionCase = (coini, coinj)
            coini_lastCase = last_i // 3
            coinj_lastCase = last_j // 3
            region_lastCase = (coini_lastCase, coinj_lastCase)

            if last_v in case[2]:
                if (
                        case[0] == last_i or case[1] == last_j or (regionCase == region_lastCase)):
                    case[2].remove(last_v)

        # raise NotImplementedError()

    def commit_one_var(self):
        """À COMPLÉTER
        Cette méthode cherche une case pour laquelle il n'y a plus qu'une seule possibilité.
        Si elle en trouve une, elle écrit cette unique valeur possible dans la grille
        et renvoie la position de la case et la valeur inscrite.
        :return: Le numéro de ligne, de colonne et la valeur inscrite dans la case
        ou ``None`` si aucune case n'a pu être remplie.
        :rtype: tuple of int or None
        """

        for case in self.possiblesChoices:
            if len(case[2]) == 1:
                self.grid.write(case[0], case[1], case[2])
                print("Case trouvée avec une seule solution")
                res = case[0], case[1], case[2]
                self.possiblesChoices.remove(case)
                return res

        return None

        # raise NotImplementedError()

    def solve_step(self):  # ok je pense
        """À COMPLÉTER
        Cette méthode alterne entre l'affectation de case pour lesquelles il n'y a plus qu'une possibilité
        et l'élimination des nouvelles valeurs impossibles pour les autres cases concernées.
        Elle répète cette alternance tant qu'il reste des cases à remplir,
        et correspond à la résolution de Sudokus dits «simple».
        *Variante avancée: en plus de vérifier s'il ne reste plus qu'une seule possibilité pour une case,
        il est aussi possible de vérifier s'il ne reste plus qu'une seule position valide pour une certaine valeur
        sur chaque ligne, chaque colonne et dans chaque région*
        """
        continuer = True
        alternance = True
        while continuer:
            caseUneSeulePossibilite = self.commit_one_var()
            if caseUneSeulePossibilite is not None:
                if alternance:
                    self.grid.write(caseUneSeulePossibilite[0], caseUneSeulePossibilite[1], caseUneSeulePossibilite[2])
                    alternance = False
                else:
                    self.reduce_domains(caseUneSeulePossibilite[0], caseUneSeulePossibilite[1],
                                        caseUneSeulePossibilite[2])
                    alternance = True
            else:
                continuer = False
        # J'EN AI MARRE

        # raise NotImplementedError()

    def is_valid(self):
        """À COMPLÉTER
        Cette méthode vérifie qu'il reste des possibilités pour chaque case vide
        dans la solution partielle actuelle.
        :return: Un booléen indiquant si la solution partielle actuelle peut encore mener à une solution valide
        :rtype: bool
        """
        for case in self.possiblesChoices:
            if len(case[2]) == 0:
                print("Sudoku non solvable")
                return False

        return True

        # raise NotImplementedError()

    def is_solved(self):
        """À COMPLÉTER
        Cette méthode vérifie si la solution actuelle est complète,
        c'est-à-dire qu'il ne reste plus aucune case vide.
        :return: Un booléen indiquant si la solution actuelle est complète.
        :rtype: bool
        """

        if len(self.grid.get_empty_pos()) == 0:
            return True
        else:
            return False

        # raise NotImplementedError()

    def branch(self):
        """À COMPLÉTER
        Cette méthode sélectionne une variable libre dans la solution partielle actuelle,
        et crée autant de sous-problèmes que d'affectation possible pour cette variable.
        Ces sous-problèmes seront sous la forme de nouvelles instances de solver
        initialisées avec une grille partiellement remplie.
        *Variante avancée: Renvoyez un générateur au lieu d'une liste.*
        *Variante avancée: Un choix judicieux de variable libre,
        ainsi que l'ordre dans lequel les affectations sont testées
        peut fortement améliorer les performances de votre solver.*
        :return: Une liste de sous-problèmes ayant chacun une valeur différente pour la variable choisie
        :rtype: list of SudokuSolver
        """
        # utiliser variable possibleChoices
        var = SudokuSolver(self.grid)
        res = list()

        for i in self.possiblesChoices:
            var.grid.write(i[0], i[1], i[2])
            if var.is_valid():
                res.append(var)

        return res
        # raise NotImplementedError()

    def solve(self):  # ok je pense
        """
        Cette méthode implémente la fonction principale de la programmation par contrainte.
        Elle cherche d'abord à affiner au mieux la solution partielle actuelle par un appel à ``solve_step``.
        Si la solution est complète, elle la retourne.
        Si elle est invalide, elle renvoie ``None`` pour indiquer un cul-de-sac dans la recherche de solution
        et déclencher un retour vers la précédente solution valide.
        Sinon, elle crée plusieurs sous-problèmes pour explorer différentes possibilités
        en appelant récursivement ``solve`` sur ces sous-problèmes.
        :return: Une solution pour la grille de Sudoku donnée à l'initialisation du solver
        (ou None si pas de solution)
        :rtype: SudokuGrid or None
        """
        self.solve_step()
        if self.is_solved():
            return self.grid
        elif not self.is_valid():
            return None
        else:
            list = self.branch()
            for i in list:
                temp = i.solve()
                if temp is not None:
                    return temp

        # raise NotImplementedError()
