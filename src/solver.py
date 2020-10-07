from grid import SudokuGrid


class SudokuSolver:

    def __init__(self, grid_game):

        self.grid = grid_game
        self.possible_choices = []
        self.reduce_all_domains()

        # raise NotImplementedError()

    def reduce_all_domains(self):
        """À COMPLÉTER
             Cette méthode devrait être appelée à l'initialisation
             et élimine toutes les valeurs impossibles pour chaque case vide.
             *Indication: Vous pouvez utiliser les fonction ``get_row``, ``get_col`` et ``get_region`` de la grille*
             """
        cases_vides = self.grid.get_empty_pos()

        for i in range(len(cases_vides)):
                    s_list = set(range(1, 10))
                    possible_lines = set(self.grid.get_row(cases_vides[i][0]))
                    possible_col = set(self.grid.get_col(cases_vides[i][1]))
                    possible_reg = set(self.grid.get_region(cases_vides[i][0], cases_vides[i][1]))
                    list_possibles = s_list - possible_col - possible_lines - possible_reg

                    if len(list_possibles) == 0:
                        print("No Possibilities for [", cases_vides[i][0], "][", cases_vides[i][1], "]")
                    else:
                        self.possible_choices.append(((cases_vides[i][0], cases_vides[i][1]), list(list_possibles)))

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
        for case in self.possible_choices:

            coin_i = case[0][0] // 3
            coin_j = case[0][1] // 3
            region_case = (coin_i, coin_j)
            coin_i_last = last_i // 3
            coin_j_last = last_j // 3
            region_last = (coin_i_last, coin_j_last)

            if last_v in case[1]:
                if (case[0][0] == last_i) or (case[0][1] == last_j) or (region_case == region_last):
                    case[1].remove(last_v)

    def commit_one_var(self):
        """À COMPLÉTER
               Cette méthode cherche une case pour laquelle il n'y a plus qu'une seule possibilité.
               Si elle en trouve une, elle écrit cette unique valeur possible dans la grille
               et renvoie la position de la case et la valeur inscrite.
               :return: Le numéro de ligne, de colonne et la valeur inscrite dans la case
               ou ``None`` si aucune case n'a pu être remplie.
               :rtype: tuple of int or None
               """
        for case in self.possible_choices:
            if len(case[1]) == 1:
                self.grid[case[0][0]][case[0][1]] = case[1]
                return (case[0][0], case[0][1], case[1])

        return None

    def solve_step(self):
        """À COMPLÉTER
             Cette méthode alterne entre l'affectation de case pour lesquelles il n'y a plus qu'une possibilité
             et l'élimination des nouvelles valeurs impossibles pour les autres cases concernées.
             Elle répète cette alternance tant qu'il reste des cases à remplir,
             et correspond à la résolution de Sudokus dits «simple».
             *Variante avancée: en plus de vérifier s'il ne reste plus qu'une seule possibilité pour une case,
             il est aussi possible de vérifier s'il ne reste plus qu'une seule position valide pour une certaine valeur
             sur chaque ligne, chaque colonne et dans chaque région*
             """

        """continuer = True
        while continuer:
            caseUneSeulePossibilite = self.commit_one_var()
            if caseUneSeulePossibilite is not None:
               self.grid[caseUneSeulePossibilite[0]][caseUneSeulePossibilite[1]] = caseUneSeulePossibilite[2]
               self.reduce_domains(caseUneSeulePossibilite[0], caseUneSeulePossibilite[1], caseUneSeulePossibilite[2])
        """
        raise NotImplementedError()

    def is_valid(self):
        """À COMPLÉTER
               Cette méthode vérifie qu'il reste des possibilités pour chaque case vide
               dans la solution partielle actuelle.
               :return: Un booléen indiquant si la solution partielle actuelle peut encore mener à une solution valide
               :rtype: bool
               """
        for case in self.possible_choices:
            if len(case[1]) == 0:
                return False

        return True

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
        raise NotImplementedError()

    def solve(self):
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
        raise NotImplementedError()


if __name__ == "__main__":

    grid = SudokuGrid("349000000000000700000509002200095007001000400800720005100402000008000000000000376")
    solve = SudokuSolver(grid)
    print(solve.is_valid())
    print(solve.commit_one_var())
    print(solve.is_solved())


